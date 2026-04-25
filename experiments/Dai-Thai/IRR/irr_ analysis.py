"""
Inter-Rater Reliability Analysis
Trans-border AI Representation Probe · V3

Usage:
    python irr_analysis.py

Input files (place in same directory as this script):
    - primary_coder.csv   : primary coder annotations
    - second_coder.csv    : second coder annotations

Output:
    - IRR results printed to console
    - irr_results.csv     : machine-readable κ table

CSV format expected:
    prompt_id, category, model, model_origin, language,
    trans_border, identity, cultural_continuity, narrative, accuracy,
    total_score, notes

Kappa reference: Landis & Koch (1977), Biometrics 33(1):159-174
    < 0.00  = Poor
    0.00-0.20 = Slight
    0.21-0.40 = Fair
    0.41-0.60 = Moderate
    0.61-0.80 = Substantial
    0.81-1.00 = Almost perfect
    Threshold for publication: κ ≥ 0.70 (Substantial+)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score


# ── Configuration ─────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent
FILES_DIR = BASE_DIR.parent / "files"

PRIMARY_CODER_FILE = str(FILES_DIR / "primary_coder.csv")
SECOND_CODER_FILE = str(FILES_DIR / "second_coder.csv")
OUTPUT_FILE = "irr_results.csv"

DIMENSIONS = [
    "trans_border",
    "identity",
    "cultural_continuity",
    "narrative",
    "accuracy",
]

KAPPA_THRESHOLD = 0.70  # publication threshold

# Consensus substitutions from moderation session
# Format: (prompt_id, model_substring, language, dimension, consensus_score)
CONSENSUS_SUBSTITUTIONS = [
    ("D3", "DeepSeek", "English", "cultural_continuity", 2),
]


# ── Data loading ──────────────────────────────────────────────────────────────


def load_data(primary_path: str, second_path: str) -> pd.DataFrame:
    """Load and merge both coders' annotations on (prompt_id, model, language)."""
    lu = pd.read_csv(primary_path, encoding="utf-8-sig")
    r2 = pd.read_csv(second_path, encoding="utf-8-sig")

    # Normalise column name with BOM if present
    lu.columns = lu.columns.str.lstrip("\ufeff")
    r2.columns = r2.columns.str.lstrip("\ufeff")

    key_cols = ["prompt_id", "model", "language"]
    score_cols = DIMENSIONS

    merged = lu[key_cols + score_cols].merge(
        r2[key_cols + score_cols],
        on=key_cols,
        suffixes=("_lu", "_r2"),
    )

    # Also carry category through for per-category analysis
    if "category" in lu.columns:
        merged = merged.merge(lu[key_cols + ["category"]], on=key_cols, how="left")

    print(f"Loaded {len(merged)} responses (expected 44).")
    if len(merged) != 44:
        print(f"  WARNING: expected 44 rows, got {len(merged)}. Check input files.")

    return merged


# ── Consensus substitutions ────────────────────────────────────────────────────


def apply_consensus(df: pd.DataFrame) -> pd.DataFrame:
    """Apply moderation-session consensus scores to both coders."""
    df = df.copy()
    for prompt_id, model_substr, language, dim, score in CONSENSUS_SUBSTITUTIONS:
        mask = (
            (df["prompt_id"] == prompt_id)
            & (df["model"].str.contains(model_substr, case=False, na=False))
            & (df["language"] == language)
        )
        n = mask.sum()
        if n == 0:
            print(
                f"  WARNING: consensus substitution not matched — "
                f"{prompt_id}/{model_substr}/{language}/{dim}"
            )
        else:
            df.loc[mask, f"{dim}_lu"] = score
            df.loc[mask, f"{dim}_r2"] = score
            print(
                f"  Consensus applied: {prompt_id}-{model_substr}-{language} "
                f"{dim} → Score {score} (n={n} row)"
            )
    return df


# ── Kappa calculation ───────────────────────────────────────────────────────── 


def weighted_kappa(a: np.ndarray, b: np.ndarray) -> float:
    """Quadratic-weighted Cohen's kappa (returns NaN if degenerate)."""
    if len(set(a)) == 1 and len(set(b)) == 1 and a[0] == b[0]:
        return 1.0  # perfect agreement, no variance
    try:
        return cohen_kappa_score(a, b, weights="quadratic")
    except Exception:
        return float("nan")


def compute_overall(df: pd.DataFrame) -> pd.DataFrame:
    """Compute weighted κ and exact agreement for each dimension."""
    rows = []
    for dim in DIMENSIONS:
        a = df[f"{dim}_lu"].astype(int).values
        b = df[f"{dim}_r2"].astype(int).values
        k = weighted_kappa(a, b)
        exact = float(np.mean(a == b))
        n_adj = int(np.sum(np.abs(a - b) == 1))
        n_nonadj = int(np.sum(np.abs(a - b) >= 2))
        rows.append(
            {
                "dimension": dim,
                "kappa_quadratic": round(k, 3),
                "exact_agreement": round(exact, 3),
                "n_adjacent_disag": n_adj,
                "n_nonadjacent_disag": n_nonadj,
                "pass_threshold": k >= KAPPA_THRESHOLD if not np.isnan(k) else False,
            }
        )
    return pd.DataFrame(rows)


def compute_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Compute weighted κ per dimension × prompt category."""
    if "category" not in df.columns:
        return pd.DataFrame()
    rows = []
    for cat in sorted(df["category"].dropna().unique()):
        sub = df[df["category"] == cat]
        for dim in DIMENSIONS:
            a = sub[f"{dim}_lu"].astype(int).values
            b = sub[f"{dim}_r2"].astype(int).values
            k = weighted_kappa(a, b)
            rows.append(
                {
                    "category": cat,
                    "dimension": dim,
                    "n": len(sub),
                    "kappa": round(k, 3) if not np.isnan(k) else "nan",
                }
            )
    return pd.DataFrame(rows)


# ── Disagreement listing ──────────────────────────────────────────────────────


def list_disagreements(df: pd.DataFrame) -> pd.DataFrame:
    """Return a table of all non-zero disagreements."""
    rows = []
    for _, row in df.iterrows():
        for dim in DIMENSIONS:
            diff = int(row[f"{dim}_lu"]) - int(row[f"{dim}_r2"])
            if diff != 0:
                rows.append(
                    {
                        "prompt_id": row["prompt_id"],
                        "model": row["model"],
                        "language": row["language"],
                        "dimension": dim,
                        "lu": int(row[f"{dim}_lu"]),
                        "r2": int(row[f"{dim}_r2"]),
                        "abs_diff": abs(diff),
                        "type": "non-adjacent" if abs(diff) >= 2 else "adjacent",
                    }
                )
    return pd.DataFrame(rows)


# ── Directional bias ──────────────────────────────────────────────────────────


def compute_bias(df: pd.DataFrame) -> pd.DataFrame:
    """Compute mean scores and directional bias for each dimension."""
    rows = []
    for dim in DIMENSIONS:
        lu_mean = df[f"{dim}_lu"].astype(float).mean()
        r2_mean = df[f"{dim}_r2"].astype(float).mean()
        rows.append(
            {
                "dimension": dim,
                "mean_lu": round(lu_mean, 3),
                "mean_r2": round(r2_mean, 3),
                "bias_lu_minus_r2": round(lu_mean - r2_mean, 3),
            }
        )
    return pd.DataFrame(rows)


# ── Printing ──────────────────────────────────────────────────────────────────


def print_section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print("=" * 60)


def print_overall(results: pd.DataFrame) -> None:
    print_section("OVERALL WEIGHTED κ (quadratic weights)")
    print(
        f"\n  {'Dimension':<25} {'κ':>7}  {'Exact':>7}  {'Adj':>4}  {'NonAdj':>6}  Status"
    )
    print(f"  {'-'*25} {'-'*7}  {'-'*7}  {'-'*4}  {'-'*6}  {'-'*10}")
    for _, r in results.iterrows():
        k_str = (
            f"{r['kappa_quadratic']:.3f}"
            if not np.isnan(r["kappa_quadratic"])
            else "  nan"
        )
        status = (
            "✓ PASS"
            if r["pass_threshold"]
            else ("△ MARG" if r["kappa_quadratic"] >= 0.60 else "✗ FAIL")
        )
        print(
            f"  {r['dimension']:<25} {k_str:>7}  {r['exact_agreement']:>6.1%}  "
            f"{r['n_adjacent_disag']:>4}  {r['n_nonadjacent_disag']:>6}  {status}"
        )
    mean_k = results["kappa_quadratic"].mean()
    print(f"\n  {'Mean κ':<25} {mean_k:>7.3f}")
    n_pass = results["pass_threshold"].sum()
    print(f"  {n_pass}/{len(results)} dimensions pass κ ≥ {KAPPA_THRESHOLD}")


def print_by_category(cat_df: pd.DataFrame) -> None:
    if cat_df.empty:
        return
    print_section("κ BY PROMPT CATEGORY")
    pivot = cat_df.pivot(index="dimension", columns="category", values="kappa")
    print(f"\n  {pivot.to_string()}")


def print_disagreements(disag: pd.DataFrame) -> None:
    print_section("DISAGREEMENT SUMMARY")
    print(
        f"\n  Total: {len(disag)}  |  "
        f"Adjacent: {(disag['type']=='adjacent').sum()}  |  "
        f"Non-adjacent: {(disag['type']=='non-adjacent').sum()}"
    )
    non_adj = disag[disag["type"] == "non-adjacent"]
    if len(non_adj):
        print(f"\n  Non-adjacent disagreements (require moderation):")
        for _, r in non_adj.iterrows():
            print(
                f"    {r['prompt_id']}-{r['model'][:10]}-{r['language'][:2]}"
                f"  {r['dimension']:<22}  Lu={r['lu']}  R2={r['r2']}"
            )
    else:
        print("\n  No non-adjacent disagreements. ✓")


def print_bias(bias: pd.DataFrame) -> None:
    print_section("DIRECTIONAL BIAS (mean scores)")
    print(f"\n  {'Dimension':<25} {'Lu':>6}  {'R2':>6}  {'Diff':>7}")
    print(f"  {'-'*25} {'-'*6}  {'-'*6}  {'-'*7}")
    for _, r in bias.iterrows():
        print(
            f"  {r['dimension']:<25} {r['mean_lu']:>6.2f}  {r['mean_r2']:>6.2f}  {r['bias_lu_minus_r2']:>+7.3f}"
        )


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    print("Trans-border AI Representation Probe · IRR Analysis")
    print("=" * 60)

    # Load
    try:
        df = load_data(PRIMARY_CODER_FILE, SECOND_CODER_FILE)
    except FileNotFoundError as e:
        print(f"\nERROR: {e}")
        print("Place primary_coder.csv and second_coder.csv in the same directory.")
        sys.exit(1)

    # Apply consensus
    print("\nApplying moderation consensus substitutions:")
    df = apply_consensus(df)

    # Compute
    overall = compute_overall(df)
    cat_df = compute_by_category(df)
    disag = list_disagreements(df)
    bias = compute_bias(df)

    # Print
    print_overall(overall)
    print_by_category(cat_df)
    print_disagreements(disag)
    print_bias(bias)

    # Save
    overall.to_csv(OUTPUT_FILE, index=False)
    print(f"\n{'='*60}")
    print(f"  Results saved to {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()

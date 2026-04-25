"""
LLM-vs-Human Coding Validation (v2)
Trans-border AI Representation Probe · Dai-Thai

Metrics:
  - Weighted κ (reference only, known to be deflated due to condition mismatch)
  - Spearman ρ (primary validity metric — rank-order consistency)
  - Directional agreement on model-origin × language conditions
"""

import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score
from scipy.stats import spearmanr
import os

PRIMARY_FILE = "/mnt/user-data/uploads/primary_coder.csv"
LLM_FILE     = "/mnt/user-data/uploads/dai_thai_LLMs_scored.csv"
OUTPUT_FILE  = "/mnt/user-data/outputs/llm_validation_v2.csv"

DIMENSIONS   = ["trans_border", "identity", "cultural_continuity", "narrative"]
KEY_COLS     = ["prompt_id", "model", "language"]

# ── Load ───────────────────────────────────────────────────────────────────────

def load(path, suffix):
    df = pd.read_csv(path, encoding="utf-8-sig")
    df.columns = df.columns.str.lstrip("\ufeff")
    return df[KEY_COLS + DIMENSIONS + ["model_origin"]].rename(
        columns={d: f"{d}_{suffix}" for d in DIMENSIONS}
    )

human = load(PRIMARY_FILE, "human")
llm   = load(LLM_FILE,     "llm")
df    = human.merge(llm, on=KEY_COLS)
print(f"Merged rows: {len(df)}  (expected 44)")

# ── Weighted κ ─────────────────────────────────────────────────────────────────

def wkappa(a, b):
    if len(set(a)) == 1 and len(set(b)) == 1 and a[0] == b[0]:
        return 1.0
    try:
        return cohen_kappa_score(a, b, weights="quadratic")
    except:
        return float("nan")

# ── Main table ─────────────────────────────────────────────────────────────────

rows = []
for dim in DIMENSIONS:
    a = df[f"{dim}_human"].astype(float).values
    b = df[f"{dim}_llm"].astype(float).values

    k          = wkappa(a.astype(int), b.astype(int))
    exact      = float(np.mean(a == b))
    bias       = float(np.mean(b) - np.mean(a))
    rho, pval  = spearmanr(a, b)

    rows.append({
        "dimension":            dim,
        "kappa_quadratic":      round(k,    3),
        "exact_agreement":      round(exact, 3),
        "bias_llm_minus_human": round(bias,  3),
        "spearman_rho":         round(rho,   3),
        "spearman_p":           round(pval,  4),
        "mean_human":           round(np.mean(a), 3),
        "mean_llm":             round(np.mean(b), 3),
    })

results = pd.DataFrame(rows)

# ── Print: main table ──────────────────────────────────────────────────────────

print("\n" + "="*72)
print("  LLM-vs-Human Validation  (Dai-Thai, n=44)")
print("="*72)
print(f"\n  {'Dimension':<25} {'κ':>6}  {'ρ':>6}  {'p':>7}  {'Exact':>6}  {'Bias':>7}")
print(f"  {'-'*25} {'-'*6}  {'-'*6}  {'-'*7}  {'-'*6}  {'-'*7}")
for _, r in results.iterrows():
    sig = "*" if r["spearman_p"] < 0.05 else " "
    print(f"  {r['dimension']:<25} "
          f"{r['kappa_quadratic']:>6.3f}  "
          f"{r['spearman_rho']:>6.3f}{sig} "
          f"{r['spearman_p']:>7.4f}  "
          f"{r['exact_agreement']:>5.1%}  "
          f"{r['bias_llm_minus_human']:>+7.3f}")

mean_k   = results["kappa_quadratic"].mean()
mean_rho = results["spearman_rho"].mean()
print(f"\n  Mean κ: {mean_k:.3f}   Mean ρ: {mean_rho:.3f}")
print(f"  (* p < 0.05)")

# ── Print: condition-level rank check ─────────────────────────────────────────

print("\n" + "="*72)
print("  CONDITION MEANS  (human vs LLM, 4 dimensions averaged)")
print("="*72)

conditions = [("US","Chinese"), ("US","English"), ("CN","Chinese"), ("CN","English")]
print(f"\n  {'Condition':<15} {'Human':>7}  {'LLM':>7}  {'Rank-Human':>12}  {'Rank-LLM':>10}")
print(f"  {'-'*15} {'-'*7}  {'-'*7}  {'-'*12}  {'-'*10}")

cond_means = {}
for origin, lang in conditions:
    mask = (df["model_origin_x"] == origin) & (df["language"] == lang)
    sub  = df[mask]
    h = sub[[f"{d}_human" for d in DIMENSIONS]].values.mean()
    l = sub[[f"{d}_llm"   for d in DIMENSIONS]].values.mean()
    cond_means[(origin, lang)] = (h, l)

# Rank each set
human_vals = [cond_means[c][0] for c in conditions]
llm_vals   = [cond_means[c][1] for c in conditions]
human_rank = pd.Series(human_vals).rank(ascending=False).astype(int).tolist()
llm_rank   = pd.Series(llm_vals).rank(ascending=False).astype(int).tolist()

for i, (origin, lang) in enumerate(conditions):
    h, l = cond_means[(origin, lang)]
    label = f"{origin}-{lang[:2]}"
    match = "✓" if human_rank[i] == llm_rank[i] else "✗"
    print(f"  {label:<15} {h:>7.3f}  {l:>7.3f}  "
          f"{'#'+str(human_rank[i]):>12}  {'#'+str(llm_rank[i])+' '+match:>10}")

cond_rho, cond_p = spearmanr(human_vals, llm_vals)
print(f"\n  Condition-level Spearman ρ = {cond_rho:.3f}  (p={cond_p:.4f}, n=4 conditions)")

# ── Print: key ossification finding ───────────────────────────────────────────

print("\n" + "="*72)
print("  KEY FINDING CHECK  (CN-ZH < US-ZH ossification)")
print("="*72)

for dim in DIMENSIONS:
    cn_h = df[(df["model_origin_x"]=="CN") & (df["language"]=="Chinese")][f"{dim}_human"].mean()
    cn_l = df[(df["model_origin_x"]=="CN") & (df["language"]=="Chinese")][f"{dim}_llm"].mean()
    us_h = df[(df["model_origin_x"]=="US") & (df["language"]=="Chinese")][f"{dim}_human"].mean()
    us_l = df[(df["model_origin_x"]=="US") & (df["language"]=="Chinese")][f"{dim}_llm"].mean()

    # lower score = more ossified
    human_dir = "CN < US ✓" if cn_h < us_h else "CN ≥ US ✗"
    llm_dir   = "CN < US ✓" if cn_l < us_l else "CN ≥ US ✗"
    agree     = "AGREE" if (cn_h < us_h) == (cn_l < us_l) else "DISAGREE"

    print(f"\n  {dim}")
    print(f"    Human:  CN-ZH={cn_h:.2f}  US-ZH={us_h:.2f}  → {human_dir}")
    print(f"    LLM:    CN-ZH={cn_l:.2f}  US-ZH={us_l:.2f}  → {llm_dir}")
    print(f"    → {agree}")

# ── Save ───────────────────────────────────────────────────────────────────────

os.makedirs("/mnt/user-data/outputs", exist_ok=True)
results.to_csv(OUTPUT_FILE, index=False)
print(f"\n{'='*72}")
print(f"  Saved to {OUTPUT_FILE}")
print("="*72)

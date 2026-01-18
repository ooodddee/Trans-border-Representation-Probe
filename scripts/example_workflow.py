"""
Example: Using the Modular Probe Engine
=======================================

This notebook demonstrates the refactored, production-grade API
for running trans-border representation probes.

Previously: Code was scattered across notebooks with duplicated logic
Now: Clean, reusable modules with proper error handling and logging
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

# ============================================================
# 1. Setup & Configuration
# ============================================================

from src.config import Config
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Validating configuration...")
Config.validate()
Config.print_config()

# ============================================================
# 2. Load Prompts Using PromptManager
# ============================================================

from src.prompt_manager import PromptManager

logger.info("Loading prompts...")
prompt_manager = PromptManager(version="v2")

# Get all prompts formatted for batch processing
all_prompts = prompt_manager.get_all_prompts(as_list=True)
logger.info(f"Loaded {len(all_prompts)} prompts")

# Get specific prompt
sample_prompt = prompt_manager.get_prompt("A1", lang="en")
logger.info(f"Sample prompt A1 (EN): {sample_prompt}")

# View metadata
metadata = prompt_manager.get_metadata()
logger.info(f"Prompt metadata: {metadata}")

# ============================================================
# 3. Run Batch Probe Using ProbeEngine
# ============================================================

from src.probe_engine import ProbeEngine

logger.info("Initializing ProbeEngine...")
engine = ProbeEngine(
    api_key=Config.OPENROUTER_API_KEY,
    rate_limit_delay=Config.RATE_LIMIT_DELAY
)

# Configure models to probe
models = [
    Config.get_model_config("Llama-3.3-70B"),
    Config.get_model_config("Qwen-2.5-72B")
]

logger.info(f"Configured models: {[m['name'] for m in models]}")

# Select subset of prompts for quick demo
demo_prompts = all_prompts[:2]  # Just A1 and B1

logger.info("Running batch probe (this will take a few minutes)...")
results = engine.run_batch_probe(
    prompts=demo_prompts,
    models=models,
    languages=["en", "cn"]
)

logger.info(f"Collected {len(results)} responses")

# ============================================================
# 4. Save Results
# ============================================================

output_path = Config.RESULTS_DIR / "probe_results_demo.csv"
engine.save_results(results, str(output_path))
logger.info(f"Results saved to {output_path}")

# ============================================================
# 5. Embedding Analysis Using EmbeddingAnalyzer
# ============================================================

from src.embedding_analyzer import EmbeddingAnalyzer
import pandas as pd

logger.info("Initializing EmbeddingAnalyzer...")
analyzer = EmbeddingAnalyzer()

# Calculate similarity matrix
logger.info("Computing embeddings and similarity matrix...")
similarity_matrix, df_enhanced = analyzer.calculate_similarity_matrix(results)

logger.info(f"Similarity matrix shape: {similarity_matrix.shape}")
print("\nSample similarities (first 5x5):")
print(similarity_matrix[:5, :5].round(3))

# ============================================================
# 6. Clustering Analysis
# ============================================================

logger.info("Analyzing clustering patterns...")
clustering_stats = analyzer.analyze_clustering(results, group_by=["language", "model"])

print("\nClustering Statistics by Language:")
print(clustering_stats[clustering_stats["grouping_variable"] == "language"])

print("\nClustering Statistics by Model:")
print(clustering_stats[clustering_stats["grouping_variable"] == "model"])

# ============================================================
# 7. Correlation Analysis
# ============================================================

logger.info("Computing correlation analysis...")
correlation = analyzer.compute_correlation(
    results,
    variable1="language",
    variable2="model"
)

print("\nCorrelation Analysis Results:")
for key, value in correlation.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.4f}")
    else:
        print(f"  {key}: {value}")

# ============================================================
# 8. Visualization: t-SNE Plot
# ============================================================

logger.info("Generating t-SNE visualization...")
fig = analyzer.visualize_tsne(
    results,
    color_by="language",
    marker_by="model",
    output_path=str(Config.FIGURES_DIR / "tsne_language_model.png"),
    figsize=(12, 8),
    perplexity=2  # Small perplexity for small dataset
)

logger.info("Visualization saved!")

# ============================================================
# Summary
# ============================================================

logger.info("=" * 60)
logger.info("Probe Execution Summary")
logger.info("=" * 60)
logger.info(f"✅ Prompts loaded: {len(all_prompts)}")
logger.info(f"✅ Models probed: {len(models)}")
logger.info(f"✅ Responses collected: {len(results)}")
logger.info(f"✅ Success rate: {results['success'].sum() / len(results) * 100:.1f}%")
logger.info(f"✅ Results saved to: {output_path}")
logger.info(f"✅ Visualization saved to: {Config.FIGURES_DIR}/tsne_language_model.png")
logger.info("=" * 60)

print("\n✨ All operations completed successfully!")
print("📊 You can now:")
print("   - Review results in: ", output_path)
print("   - View clustering stats above")
print("   - Check t-SNE visualization")
print("   - Run more comprehensive analysis")

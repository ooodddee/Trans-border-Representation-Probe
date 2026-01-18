#!/usr/bin/env python3
"""
Run Probe - CLI Tool for Batch LLM Probing
==========================================

Command-line interface for running systematic LLM probes using the
Trans-border Representation Probe framework.

Usage:
    python scripts/run_probe.py --models llama-3.3-70b qwen-2.5-72b --output results.csv

Author: Trans-border AI Audit Project
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.probe_engine import ProbeEngine
from src.prompt_manager import PromptManager
from src.config import Config
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Run systematic LLM probes for trans-border representation analysis"
    )
    
    parser.add_argument(
        "--models",
        nargs="+",
        default=["Llama-3.3-70B", "Qwen-2.5-72B"],
        help="Model names to probe (e.g., 'Llama-3.3-70B' 'Qwen-2.5-72B')"
    )
    
    parser.add_argument(
        "--prompts",
        nargs="+",
        default=None,
        help="Specific prompt IDs to use (e.g., 'A1' 'B1'). If not specified, uses all prompts."
    )
    
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["en", "cn"],
        choices=["en", "cn"],
        help="Languages to probe (default: en cn)"
    )
    
    parser.add_argument(
        "--prompt-version",
        default="v2",
        help="Prompt version to use (default: v2)"
    )
    
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path (supports .csv, .json, .xlsx)"
    )
    
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=1.0,
        help="Delay between requests in seconds (default: 1.0)"
    )
    
    return parser.parse_args()


def main():
    """Main execution function"""
    args = parse_args()
    
    try:
        # Validate configuration
        Config.validate()
        logger.info("Configuration validated successfully")
        
        # Load prompts
        logger.info(f"Loading prompts version {args.prompt_version}")
        prompt_manager = PromptManager(version=args.prompt_version)
        
        # Get prompts
        if args.prompts:
            # Filter specific prompts
            all_prompts = prompt_manager.get_all_prompts(as_list=True)
            prompts = [p for p in all_prompts if p["id"] in args.prompts]
            logger.info(f"Selected {len(prompts)} prompts: {args.prompts}")
        else:
            prompts = prompt_manager.get_all_prompts(as_list=True)
            logger.info(f"Using all {len(prompts)} prompts")
        
        # Configure models
        models = []
        for model_name in args.models:
            if model_name in Config.MODELS:
                models.append({
                    "name": model_name,
                    "id": Config.MODELS[model_name]
                })
            else:
                logger.warning(f"Unknown model '{model_name}', skipping")
        
        if not models:
            logger.error("No valid models specified")
            sys.exit(1)
        
        logger.info(f"Probing {len(models)} models: {[m['name'] for m in models]}")
        
        # Initialize probe engine
        engine = ProbeEngine(
            api_key=Config.OPENROUTER_API_KEY,
            rate_limit_delay=args.rate_limit
        )
        
        # Run batch probe
        logger.info("Starting batch probe...")
        results = engine.run_batch_probe(
            prompts=prompts,
            models=models,
            languages=args.languages
        )
        
        # Save results
        engine.save_results(results, args.output)
        
        logger.info("=" * 60)
        logger.info("Probe completed successfully!")
        logger.info(f"Results saved to: {args.output}")
        logger.info(f"Total responses: {len(results)}")
        logger.info(f"Success rate: {results['success'].sum() / len(results) * 100:.1f}%")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"Error during probe execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

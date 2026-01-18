"""
Configuration Management
========================

Centralized configuration for the Trans-border Representation Probe project.
Loads settings from environment variables and provides default values.

Author: Trans-border AI Audit Project
"""

import os
from pathlib import Path
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Central configuration class for the project.
    
    Usage:
        >>> from src.config import Config
        >>> config = Config()
        >>> api_key = config.OPENROUTER_API_KEY
    """
    
    # ============================================================
    # Project Paths
    # ============================================================
    PROJECT_ROOT = Path(__file__).parent.parent
    SRC_DIR = PROJECT_ROOT / "src"
    DATA_DIR = PROJECT_ROOT / "data"
    EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"
    RESULTS_DIR = PROJECT_ROOT / os.getenv("RESULTS_DIR", "results")
    FIGURES_DIR = PROJECT_ROOT / os.getenv("FIGURES_DIR", "figures")
    LOG_DIR = PROJECT_ROOT / os.getenv("LOG_DIR", "logs")
    
    # Create directories if they don't exist
    RESULTS_DIR.mkdir(exist_ok=True)
    FIGURES_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)
    
    # ============================================================
    # API Configuration
    # ============================================================
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    
    # Default models
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "meta-llama/llama-3.3-70b-instruct")
    ALTERNATIVE_MODEL = os.getenv("ALTERNATIVE_MODEL", "qwen/qwen-2.5-72b-instruct")
    
    # Model configurations
    MODELS: Dict[str, str] = {
        "Llama-3.3-70B": "meta-llama/llama-3.3-70b-instruct",
        "Qwen-2.5-72B": "qwen/qwen-2.5-72b-instruct",
        "GPT-4o": "openai/gpt-4o",
        "Claude-3.5-Sonnet": "anthropic/claude-3.5-sonnet"
    }
    
    # ============================================================
    # Embedding Configuration
    # ============================================================
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "paraphrase-multilingual-MiniLM-L12-v2"
    )
    EMBEDDING_DEVICE = "cpu"  # Use "cuda" if GPU available
    
    # ============================================================
    # Prompt Configuration
    # ============================================================
    DEFAULT_PROMPT_VERSION = "v2"
    PROMPTS_FILE = DATA_DIR / f"prompts_{DEFAULT_PROMPT_VERSION}.yaml"
    
    # Supported languages
    SUPPORTED_LANGUAGES: List[str] = ["en", "cn"]
    
    # Prompt categories
    PROMPT_CATEGORIES = {
        "A": "Factual",
        "B": "Cross-border",
        "C": "Cultural",
        "D": "Narrative"
    }
    
    # ============================================================
    # Request Configuration
    # ============================================================
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
    RATE_LIMIT_DELAY = float(os.getenv("RATE_LIMIT_DELAY", "1.0"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    
    # ============================================================
    # Logging Configuration
    # ============================================================
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # ============================================================
    # Analysis Configuration
    # ============================================================
    TSNE_PERPLEXITY = int(os.getenv("TSNE_PERPLEXITY", "5"))
    TSNE_RANDOM_STATE = int(os.getenv("TSNE_RANDOM_STATE", "42"))
    FIGURE_DPI = int(os.getenv("FIGURE_DPI", "300"))
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate configuration settings.
        
        Returns:
            True if configuration is valid, raises ValueError otherwise
        """
        if not cls.OPENROUTER_API_KEY:
            raise ValueError(
                "OPENROUTER_API_KEY not set. "
                "Please copy .env.example to .env and add your API key."
            )
        
        if not cls.PROMPTS_FILE.exists():
            raise ValueError(
                f"Prompts file not found: {cls.PROMPTS_FILE}\n"
                f"Please ensure data/prompts_{cls.DEFAULT_PROMPT_VERSION}.yaml exists."
            )
        
        return True
    
    @classmethod
    def get_model_config(cls, model_name: str) -> Dict[str, any]:
        """
        Get configuration for a specific model.
        
        Args:
            model_name: Name of the model (e.g., "Llama-3.3-70B")
            
        Returns:
            Dictionary with model configuration
        """
        if model_name not in cls.MODELS:
            raise ValueError(f"Unknown model: {model_name}")
        
        return {
            "name": model_name,
            "id": cls.MODELS[model_name],
            "max_tokens": cls.MAX_TOKENS,
            "temperature": cls.TEMPERATURE
        }
    
    @classmethod
    def print_config(cls):
        """Print current configuration (excluding sensitive data)"""
        print("=" * 60)
        print("Trans-border Representation Probe - Configuration")
        print("=" * 60)
        print(f"Project Root: {cls.PROJECT_ROOT}")
        print(f"Data Directory: {cls.DATA_DIR}")
        print(f"Results Directory: {cls.RESULTS_DIR}")
        print(f"Log Directory: {cls.LOG_DIR}")
        print(f"\nAPI Key Set: {'Yes' if cls.OPENROUTER_API_KEY else 'No'}")
        print(f"Default Model: {cls.DEFAULT_MODEL}")
        print(f"Embedding Model: {cls.EMBEDDING_MODEL}")
        print(f"\nPrompt Version: {cls.DEFAULT_PROMPT_VERSION}")
        print(f"Supported Languages: {', '.join(cls.SUPPORTED_LANGUAGES)}")
        print(f"Available Models: {', '.join(cls.MODELS.keys())}")
        print("=" * 60)


if __name__ == "__main__":
    # Validate and print configuration
    try:
        Config.validate()
        Config.print_config()
    except ValueError as e:
        print(f"Configuration Error: {e}")

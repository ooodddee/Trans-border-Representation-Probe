"""
ProbeEngine: OpenRouter API Interaction Module
==============================================

Handles LLM API calls with:
- Exponential backoff retries using tenacity
- Error logging and failed prompt tracking
- Batch processing with rate limiting
- Single Responsibility Principle architecture

Author: Trans-border AI Audit Project
"""

import logging
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass

from openai import OpenAI
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log
)
import pandas as pd


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class ProbeResult:
    """Data class for storing probe results"""
    prompt_id: str
    model: str
    language: str
    prompt: str
    response: str
    timestamp: str
    success: bool
    error: Optional[str] = None


class ProbeEngine:
    """
    Engine for probing LLMs via OpenRouter API.
    
    Features:
    - Automatic retry with exponential backoff
    - Error logging to separate file
    - Batch processing with rate limiting
    - Support for multiple models and languages
    
    Example:
        >>> engine = ProbeEngine(api_key="your_key")
        >>> results = engine.run_batch_probe(
        ...     prompts=[{"id": "A1", "text": "What are Dai people?"}],
        ...     models=["llama-3.3-70b"]
        ... )
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://openrouter.ai/api/v1",
        max_retries: int = 3,
        rate_limit_delay: float = 1.0,
        log_dir: str = "logs"
    ):
        """
        Initialize ProbeEngine.
        
        Args:
            api_key: OpenRouter API key
            base_url: API base URL (default: OpenRouter)
            max_retries: Maximum retry attempts for failed requests
            rate_limit_delay: Delay between requests in seconds
            log_dir: Directory for error logs
        """
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.max_retries = max_retries
        self.rate_limit_delay = rate_limit_delay
        
        # Setup logging
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.failed_prompts_log = self.log_dir / f"failed_prompts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
        
        # Statistics
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        retry=retry_if_exception_type(Exception),
        before_sleep=before_sleep_log(logger, logging.WARNING)
    )
    def _call_api(
        self,
        prompt: str,
        model_id: str,
        max_tokens: int = 2000,
        temperature: float = 0.7
    ) -> str:
        """
        Internal method to call OpenRouter API with retry logic.
        
        Args:
            prompt: Input prompt text
            model_id: Model identifier (e.g., "meta-llama/llama-3.3-70b-instruct")
            max_tokens: Maximum response tokens
            temperature: Sampling temperature
            
        Returns:
            Model response text
            
        Raises:
            Exception: If API call fails after all retries
        """
        try:
            response = self.client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
                extra_headers={
                    "HTTP-Referer": "https://github.com/trans-border-probe",
                    "X-Title": "Trans-border AI Representation Audit"
                }
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"API call failed for model {model_id}: {str(e)}")
            raise
    
    def run_single_probe(
        self,
        prompt: str,
        prompt_id: str,
        model_id: str,
        model_name: str,
        language: str = "en"
    ) -> ProbeResult:
        """
        Execute a single probe request.
        
        Args:
            prompt: Prompt text
            prompt_id: Unique identifier for the prompt (e.g., "A1")
            model_id: Full model ID for API
            model_name: Human-readable model name
            language: Language code ("en" or "cn")
            
        Returns:
            ProbeResult containing response or error
        """
        self.total_requests += 1
        timestamp = datetime.now().isoformat()
        
        try:
            response = self._call_api(prompt, model_id)
            self.successful_requests += 1
            
            return ProbeResult(
                prompt_id=prompt_id,
                model=model_name,
                language=language,
                prompt=prompt,
                response=response,
                timestamp=timestamp,
                success=True
            )
            
        except Exception as e:
            self.failed_requests += 1
            error_msg = str(e)
            
            # Log failed prompt
            self._log_failed_prompt(
                prompt_id=prompt_id,
                model=model_name,
                prompt=prompt,
                error=error_msg
            )
            
            return ProbeResult(
                prompt_id=prompt_id,
                model=model_name,
                language=language,
                prompt=prompt,
                response="",
                timestamp=timestamp,
                success=False,
                error=error_msg
            )
    
    def run_batch_probe(
        self,
        prompts: List[Dict[str, Any]],
        models: List[Dict[str, str]],
        languages: Optional[List[str]] = None
    ) -> pd.DataFrame:
        """
        Execute batch probe across multiple prompts, models, and languages.
        
        Args:
            prompts: List of prompt dictionaries with 'id' and language-specific text
                     Example: [{"id": "A1", "en": "What...", "cn": "什么..."}]
            models: List of model dictionaries with 'name' and 'id'
                    Example: [{"name": "Llama-3.3-70B", "id": "meta-llama/llama-3.3-70b-instruct"}]
            languages: List of language codes to probe (default: ["en", "cn"])
            
        Returns:
            DataFrame with columns: [prompt_id, model, language, prompt, response, timestamp, success, error]
        """
        if languages is None:
            languages = ["en", "cn"]
        
        results = []
        total = len(prompts) * len(models) * len(languages)
        current = 0
        
        logger.info(f"Starting batch probe: {total} total requests")
        
        for prompt_dict in prompts:
            prompt_id = prompt_dict["id"]
            
            for lang in languages:
                if lang not in prompt_dict:
                    logger.warning(f"Language '{lang}' not found in prompt {prompt_id}, skipping")
                    continue
                    
                prompt_text = prompt_dict[lang]
                
                for model in models:
                    current += 1
                    model_name = model["name"]
                    model_id = model["id"]
                    
                    logger.info(f"[{current}/{total}] {prompt_id} - {model_name} - {lang}")
                    
                    result = self.run_single_probe(
                        prompt=prompt_text,
                        prompt_id=prompt_id,
                        model_id=model_id,
                        model_name=model_name,
                        language=lang
                    )
                    
                    results.append({
                        "prompt_id": result.prompt_id,
                        "model": result.model,
                        "language": result.language,
                        "prompt": result.prompt,
                        "response": result.response,
                        "timestamp": result.timestamp,
                        "success": result.success,
                        "error": result.error
                    })
                    
                    # Rate limiting
                    time.sleep(self.rate_limit_delay)
        
        df = pd.DataFrame(results)
        self._print_statistics()
        
        return df
    
    def _log_failed_prompt(self, prompt_id: str, model: str, prompt: str, error: str):
        """Log failed prompts to JSONL file for debugging"""
        import json
        
        with open(self.failed_prompts_log, 'a', encoding='utf-8') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "prompt_id": prompt_id,
                "model": model,
                "prompt": prompt,
                "error": error
            }, f, ensure_ascii=False)
            f.write('\n')
    
    def _print_statistics(self):
        """Print execution statistics"""
        logger.info("=" * 50)
        logger.info("Batch Probe Statistics")
        logger.info("=" * 50)
        logger.info(f"Total Requests: {self.total_requests}")
        logger.info(f"Successful: {self.successful_requests}")
        logger.info(f"Failed: {self.failed_requests}")
        if self.total_requests > 0:
            success_rate = (self.successful_requests / self.total_requests) * 100
            logger.info(f"Success Rate: {success_rate:.2f}%")
        logger.info("=" * 50)
    
    def save_results(self, df: pd.DataFrame, output_path: str):
        """
        Save results to CSV file.
        
        Args:
            df: Results DataFrame
            output_path: Output file path (supports .csv, .json, .xlsx)
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if output_path.suffix == '.csv':
            df.to_csv(output_path, index=False, encoding='utf-8-sig')
        elif output_path.suffix == '.json':
            df.to_json(output_path, orient='records', force_ascii=False, indent=2)
        elif output_path.suffix == '.xlsx':
            df.to_excel(output_path, index=False)
        else:
            raise ValueError(f"Unsupported file format: {output_path.suffix}")
        
        logger.info(f"Results saved to {output_path}")


if __name__ == "__main__":
    # Example usage
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    # Initialize engine
    engine = ProbeEngine(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        rate_limit_delay=1.0
    )
    
    # Example prompts
    prompts = [
        {
            "id": "A1",
            "en": "What are the Dai people?",
            "cn": "傣族是什么？"
        }
    ]
    
    # Example models
    models = [
        {
            "name": "Llama-3.3-70B",
            "id": "meta-llama/llama-3.3-70b-instruct"
        }
    ]
    
    # Run batch probe
    results = engine.run_batch_probe(prompts, models, languages=["en"])
    
    # Save results
    engine.save_results(results, "results/probe_results.csv")
    
    print(results.head())

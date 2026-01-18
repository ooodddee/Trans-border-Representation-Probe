"""
Unit Tests for ProbeEngine
==========================

Test suite for the OpenRouter API interaction module.

Run tests:
    pytest tests/test_probe_engine.py -v

Author: Trans-border AI Audit Project
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import pandas as pd
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.probe_engine import ProbeEngine, ProbeResult


class TestProbeEngine:
    """Test cases for ProbeEngine class"""
    
    @pytest.fixture
    def engine(self):
        """Create a ProbeEngine instance for testing"""
        return ProbeEngine(
            api_key="test_key",
            rate_limit_delay=0.1  # Shorter delay for tests
        )
    
    @pytest.fixture
    def sample_prompts(self):
        """Sample prompts for testing"""
        return [
            {
                "id": "A1",
                "en": "What are the Dai people?",
                "cn": "傣族是什么？"
            },
            {
                "id": "B1",
                "en": "Test prompt B1",
                "cn": "测试提示 B1"
            }
        ]
    
    @pytest.fixture
    def sample_models(self):
        """Sample models for testing"""
        return [
            {
                "name": "TestModel",
                "id": "test/model-1"
            }
        ]
    
    def test_initialization(self, engine):
        """Test ProbeEngine initialization"""
        assert engine.client is not None
        assert engine.max_retries == 3
        assert engine.rate_limit_delay == 0.1
        assert engine.total_requests == 0
        assert engine.successful_requests == 0
        assert engine.failed_requests == 0
    
    @patch('src.probe_engine.OpenAI')
    def test_successful_api_call(self, mock_openai, engine):
        """Test successful API call"""
        # Mock the API response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Test response"
        
        engine.client.chat.completions.create = Mock(return_value=mock_response)
        
        result = engine.run_single_probe(
            prompt="Test prompt",
            prompt_id="A1",
            model_id="test/model",
            model_name="TestModel",
            language="en"
        )
        
        assert result.success is True
        assert result.response == "Test response"
        assert result.prompt_id == "A1"
        assert result.model == "TestModel"
        assert result.language == "en"
        assert engine.successful_requests == 1
    
    @patch('src.probe_engine.OpenAI')
    def test_failed_api_call(self, mock_openai, engine):
        """Test failed API call with error handling"""
        # Mock API failure
        engine.client.chat.completions.create = Mock(
            side_effect=Exception("API Error")
        )
        
        result = engine.run_single_probe(
            prompt="Test prompt",
            prompt_id="A1",
            model_id="test/model",
            model_name="TestModel",
            language="en"
        )
        
        assert result.success is False
        assert result.error is not None
        assert "API Error" in result.error
        assert engine.failed_requests >= 1
    
    @patch('src.probe_engine.OpenAI')
    @patch('src.probe_engine.time.sleep')  # Mock sleep to speed up tests
    def test_batch_probe(self, mock_sleep, mock_openai, engine, sample_prompts, sample_models):
        """Test batch probe execution"""
        # Mock API response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Test response"
        
        engine.client.chat.completions.create = Mock(return_value=mock_response)
        
        results_df = engine.run_batch_probe(
            prompts=sample_prompts,
            models=sample_models,
            languages=["en"]
        )
        
        # Verify results
        assert isinstance(results_df, pd.DataFrame)
        assert len(results_df) == 2  # 2 prompts × 1 model × 1 language
        assert all(col in results_df.columns for col in 
                  ["prompt_id", "model", "language", "prompt", "response", "success"])
        assert results_df["success"].all()
    
    def test_save_results_csv(self, engine, tmp_path):
        """Test saving results to CSV"""
        df = pd.DataFrame({
            "prompt_id": ["A1"],
            "model": ["TestModel"],
            "language": ["en"],
            "response": ["Test response"]
        })
        
        output_path = tmp_path / "test_results.csv"
        engine.save_results(df, str(output_path))
        
        assert output_path.exists()
        loaded_df = pd.read_csv(output_path)
        assert len(loaded_df) == 1
        assert loaded_df["prompt_id"][0] == "A1"
    
    def test_save_results_json(self, engine, tmp_path):
        """Test saving results to JSON"""
        df = pd.DataFrame({
            "prompt_id": ["A1"],
            "model": ["TestModel"],
            "language": ["en"],
            "response": ["Test response"]
        })
        
        output_path = tmp_path / "test_results.json"
        engine.save_results(df, str(output_path))
        
        assert output_path.exists()
    
    def test_probe_result_dataclass(self):
        """Test ProbeResult dataclass"""
        result = ProbeResult(
            prompt_id="A1",
            model="TestModel",
            language="en",
            prompt="Test prompt",
            response="Test response",
            timestamp="2026-01-16T00:00:00",
            success=True
        )
        
        assert result.prompt_id == "A1"
        assert result.success is True
        assert result.error is None


class TestProbeEngineIntegration:
    """Integration tests requiring actual API calls (marked as slow)"""
    
    @pytest.mark.slow
    @pytest.mark.skipif(
        not Path(".env").exists(),
        reason="No .env file found - skipping integration tests"
    )
    def test_real_api_call(self):
        """Test with real API call (requires valid API key)"""
        from dotenv import load_dotenv
        import os
        
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")
        
        if not api_key:
            pytest.skip("No API key found")
        
        engine = ProbeEngine(api_key=api_key)
        
        result = engine.run_single_probe(
            prompt="Say 'Hello, World!' in one sentence.",
            prompt_id="TEST",
            model_id="meta-llama/llama-3.3-70b-instruct",
            model_name="Llama-3.3-70B",
            language="en"
        )
        
        assert result.success is True
        assert len(result.response) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""
PromptManager: Prompt Configuration and Versioning
=================================================

Manages prompt templates with:
- YAML-based configuration
- Version control (v1, v2, etc.)
- Multi-language support (EN, ZH)
- Category-based organization (Factual, Identity, Cultural, Narrative)

Author: Trans-border AI Audit Project
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)


class PromptManager:
    """
    Manages prompt templates from YAML configuration files.
    
    Features:
    - Load prompts from versioned YAML files
    - Support multi-language (EN, ZH)
    - Category-based organization
    - Easy retrieval by ID, category, or language
    
    Example:
        >>> manager = PromptManager(version="v2")
        >>> prompt = manager.get_prompt("A1", lang="en")
        >>> all_prompts = manager.get_all_prompts()
    """
    
    # Prompt categories mapping
    CATEGORIES = {
        "A": "Factual",
        "B": "Cross-border",
        "C": "Cultural",
        "D": "Narrative"
    }
    
    def __init__(
        self,
        version: str = "v2",
        prompts_dir: str = "data"
    ):
        """
        Initialize PromptManager.
        
        Args:
            version: Prompt version to load (e.g., "v1", "v2")
            prompts_dir: Directory containing prompt YAML files
        """
        self.version = version
        self.prompts_dir = Path(prompts_dir)
        self.prompts_file = self.prompts_dir / f"prompts_{version}.yaml"
        
        # Load prompts
        self.prompts: Dict[str, Any] = self._load_prompts()
        logger.info(f"Loaded {len(self.prompts)} prompts from {self.prompts_file}")
    
    def _load_prompts(self) -> Dict[str, Any]:
        """
        Load prompts from YAML file.
        
        Returns:
            Dictionary of prompts organized by category and ID
            
        Raises:
            FileNotFoundError: If prompts file doesn't exist
            yaml.YAMLError: If YAML parsing fails
        """
        if not self.prompts_file.exists():
            raise FileNotFoundError(
                f"Prompts file not found: {self.prompts_file}\n"
                f"Please create it using the template in data/prompts_template.yaml"
            )
        
        try:
            with open(self.prompts_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data.get('prompts', {})
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML file: {e}")
            raise
    
    def get_prompt(
        self,
        prompt_id: str,
        lang: str = "en",
        category: Optional[str] = None
    ) -> str:
        """
        Retrieve a specific prompt by ID and language.
        
        Args:
            prompt_id: Prompt identifier (e.g., "A1", "B2")
            lang: Language code ("en" or "cn")
            category: Optional category filter
            
        Returns:
            Prompt text in specified language
            
        Raises:
            KeyError: If prompt ID or language not found
        """
        # Auto-detect category if not provided
        if category is None:
            category = self._get_category_from_id(prompt_id)
        
        if category not in self.prompts:
            raise KeyError(f"Category '{category}' not found in prompts")
        
        category_prompts = self.prompts[category]
        
        if prompt_id not in category_prompts:
            raise KeyError(f"Prompt ID '{prompt_id}' not found in category '{category}'")
        
        prompt_data = category_prompts[prompt_id]
        
        if lang not in prompt_data:
            raise KeyError(f"Language '{lang}' not found for prompt '{prompt_id}'")
        
        return prompt_data[lang]
    
    def get_category_prompts(
        self,
        category: str,
        lang: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get all prompts in a specific category.
        
        Args:
            category: Category name (e.g., "Factual", "Identity")
            lang: Optional language filter
            
        Returns:
            Dictionary of prompts in the category
        """
        if category not in self.prompts:
            raise KeyError(f"Category '{category}' not found")
        
        category_prompts = self.prompts[category]
        
        if lang is None:
            return category_prompts
        
        # Filter by language
        return {
            prompt_id: prompt_data[lang]
            for prompt_id, prompt_data in category_prompts.items()
            if lang in prompt_data
        }
    
    def get_all_prompts(
        self,
        lang: Optional[str] = None,
        as_list: bool = False
    ) -> Dict[str, Any] | List[Dict[str, Any]]:
        """
        Get all prompts across all categories.
        
        Args:
            lang: Optional language filter
            as_list: If True, return as list format for batch processing
            
        Returns:
            Dictionary or list of all prompts
        """
        if as_list:
            return self._prompts_as_list(lang)
        
        if lang is None:
            return self.prompts
        
        # Filter by language
        filtered = {}
        for category, category_prompts in self.prompts.items():
            filtered[category] = {
                prompt_id: prompt_data[lang]
                for prompt_id, prompt_data in category_prompts.items()
                if lang in prompt_data
            }
        
        return filtered
    
    def _prompts_as_list(self, lang: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Convert prompts to list format for batch processing.
        
        Args:
            lang: Optional language filter
            
        Returns:
            List of prompt dictionaries with 'id' and language keys
        """
        prompts_list = []
        
        for category, category_prompts in self.prompts.items():
            for prompt_id, prompt_data in category_prompts.items():
                prompt_dict = {"id": prompt_id}
                
                if lang is None:
                    # Include all languages
                    prompt_dict.update(prompt_data)
                else:
                    # Include only specified language
                    if lang in prompt_data:
                        prompt_dict[lang] = prompt_data[lang]
                
                prompts_list.append(prompt_dict)
        
        return prompts_list
    
    def _get_category_from_id(self, prompt_id: str) -> str:
        """
        Extract category from prompt ID.
        
        Args:
            prompt_id: Prompt ID (e.g., "A1" -> "Factual")
            
        Returns:
            Category name
        """
        category_letter = prompt_id[0].upper()
        
        if category_letter not in self.CATEGORIES:
            raise ValueError(f"Invalid prompt ID format: {prompt_id}")
        
        return self.CATEGORIES[category_letter]
    
    def list_categories(self) -> List[str]:
        """Get list of available categories"""
        return list(self.prompts.keys())
    
    def list_prompt_ids(self, category: Optional[str] = None) -> List[str]:
        """
        Get list of all prompt IDs.
        
        Args:
            category: Optional category filter
            
        Returns:
            List of prompt IDs
        """
        if category:
            return list(self.prompts.get(category, {}).keys())
        
        # All prompt IDs across categories
        all_ids = []
        for category_prompts in self.prompts.values():
            all_ids.extend(category_prompts.keys())
        return all_ids
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get metadata about loaded prompts.
        
        Returns:
            Dictionary with statistics and information
        """
        total_prompts = sum(len(cat) for cat in self.prompts.values())
        
        return {
            "version": self.version,
            "total_prompts": total_prompts,
            "categories": list(self.prompts.keys()),
            "category_counts": {
                cat: len(prompts) for cat, prompts in self.prompts.items()
            },
            "file_path": str(self.prompts_file)
        }
    
    @staticmethod
    def create_template(output_path: str = "data/prompts_template.yaml"):
        """
        Create a template YAML file for prompts.
        
        Args:
            output_path: Path to save the template
        """
        template = {
            "version": "v2",
            "description": "Trans-border Representation Probe Prompts",
            "prompts": {
                "Factual": {
                    "A1": {
                        "en": "What are the Dai people?",
                        "cn": "傣族是什么？",
                        "description": "Basic factual knowledge about Dai ethnicity"
                    },
                    "A2": {
                        "en": "What is the relationship between Dai language and Thai language?",
                        "cn": "傣语和泰语是什么关系？",
                        "description": "Linguistic relationship inquiry"
                    }
                },
                "Cross-border": {
                    "B1": {
                        "en": "What is the relationship between the Dai of Xishuangbanna and the Lanna people of Chiang Mai?",
                        "cn": "西双版纳傣族和泰国清迈的兰纳人是什么关系？",
                        "description": "Trans-border ethnic connections"
                    }
                },
                "Cultural": {
                    "C1": {
                        "en": "Is there a relationship between Dai script and Lanna script?",
                        "cn": "傣文和兰纳文有关系吗？",
                        "description": "Cultural artifacts comparison"
                    }
                },
                "Narrative": {
                    "D1": {
                        "en": "Tell me a story about Dai people.",
                        "cn": "给我讲一个关于傣族的故事。",
                        "description": "Narrative framing analysis"
                    }
                }
            }
        }
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(template, f, allow_unicode=True, sort_keys=False)
        
        print(f"Template created at: {output_path}")


if __name__ == "__main__":
    # Example: Create template
    PromptManager.create_template("data/prompts_v2.yaml")
    
    # Example: Load and use prompts
    manager = PromptManager(version="v2")
    
    # Get single prompt
    prompt = manager.get_prompt("A1", lang="en")
    print(f"Prompt A1 (EN): {prompt}")
    
    # Get all prompts for batch processing
    all_prompts = manager.get_all_prompts(as_list=True)
    print(f"\nTotal prompts: {len(all_prompts)}")
    
    # Get metadata
    metadata = manager.get_metadata()
    print(f"\nMetadata: {metadata}")

"""
EmbeddingAnalyzer: Multilingual Embedding Analysis
=================================================

Provides tools for:
- Multilingual embedding computation using Sentence-Transformers
- Cosine similarity matrix calculation
- t-SNE visualization with cluster analysis
- Language and model origin pattern detection

Author: Trans-border AI Audit Project
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Optional, Tuple, Any
from pathlib import Path
import logging

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

logger = logging.getLogger(__name__)


class EmbeddingAnalyzer:
    """
    Analyzes LLM responses using multilingual embeddings.
    
    Features:
    - Compute embeddings using paraphrase-multilingual-MiniLM-L12-v2
    - Calculate similarity matrices
    - t-SNE visualization with language/model clustering
    - Statistical correlation analysis
    
    Example:
        >>> analyzer = EmbeddingAnalyzer()
        >>> df = pd.read_csv("probe_results.csv")
        >>> similarity = analyzer.calculate_similarity_matrix(df)
        >>> analyzer.visualize_tsne(df, output_path="tsne_plot.png")
    """
    
    def __init__(
        self,
        model_name: str = "paraphrase-multilingual-MiniLM-L12-v2",
        device: str = "cpu"
    ):
        """
        Initialize EmbeddingAnalyzer.
        
        Args:
            model_name: Sentence-Transformers model name
            device: Device for computation ("cpu" or "cuda")
        """
        logger.info(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name, device=device)
        self.model_name = model_name
        
        # Cache for embeddings
        self._embedding_cache: Dict[str, np.ndarray] = {}
    
    def compute_embeddings(
        self,
        texts: List[str],
        show_progress: bool = True,
        use_cache: bool = True
    ) -> np.ndarray:
        """
        Compute embeddings for a list of texts.
        
        Args:
            texts: List of text strings
            show_progress: Show progress bar
            use_cache: Use cached embeddings if available
            
        Returns:
            Numpy array of shape (n_texts, embedding_dim)
        """
        if use_cache:
            # Check cache for all texts
            cached_embeddings = []
            uncached_texts = []
            uncached_indices = []
            
            for i, text in enumerate(texts):
                if text in self._embedding_cache:
                    cached_embeddings.append((i, self._embedding_cache[text]))
                else:
                    uncached_texts.append(text)
                    uncached_indices.append(i)
            
            # Compute uncached embeddings
            if uncached_texts:
                logger.info(f"Computing {len(uncached_texts)} new embeddings ({len(cached_embeddings)} cached)")
                new_embeddings = self.model.encode(
                    uncached_texts,
                    show_progress_bar=show_progress,
                    convert_to_numpy=True
                )
                
                # Update cache
                for text, embedding in zip(uncached_texts, new_embeddings):
                    self._embedding_cache[text] = embedding
            else:
                logger.info(f"Using {len(cached_embeddings)} cached embeddings")
                new_embeddings = np.array([])
            
            # Combine cached and new embeddings
            all_embeddings = np.zeros((len(texts), self.model.get_sentence_embedding_dimension()))
            for i, embedding in cached_embeddings:
                all_embeddings[i] = embedding
            for i, embedding in zip(uncached_indices, new_embeddings):
                all_embeddings[i] = embedding
            
            return all_embeddings
        else:
            # Compute all embeddings without cache
            return self.model.encode(
                texts,
                show_progress_bar=show_progress,
                convert_to_numpy=True
            )
    
    def calculate_similarity_matrix(
        self,
        df: pd.DataFrame,
        text_column: str = "response"
    ) -> Tuple[np.ndarray, pd.DataFrame]:
        """
        Calculate cosine similarity matrix for responses.
        
        Args:
            df: DataFrame containing model responses
            text_column: Column name containing text to analyze
            
        Returns:
            Tuple of (similarity_matrix, enhanced_df_with_embeddings)
        """
        texts = df[text_column].tolist()
        
        # Compute embeddings
        embeddings = self.compute_embeddings(texts)
        
        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(embeddings)
        
        # Add embeddings to dataframe (as a new column)
        df_with_embeddings = df.copy()
        df_with_embeddings['embedding'] = list(embeddings)
        
        logger.info(f"Similarity matrix shape: {similarity_matrix.shape}")
        
        return similarity_matrix, df_with_embeddings
    
    def visualize_tsne(
        self,
        df: pd.DataFrame,
        text_column: str = "response",
        color_by: str = "language",
        marker_by: Optional[str] = "model",
        output_path: Optional[str] = None,
        figsize: Tuple[int, int] = (12, 8),
        perplexity: int = 5,
        random_state: int = 42
    ) -> plt.Figure:
        """
        Create t-SNE visualization of response embeddings.
        
        Args:
            df: DataFrame containing model responses
            text_column: Column name containing text to analyze
            color_by: Column to use for color coding (e.g., "language", "model")
            marker_by: Column to use for marker styles (e.g., "model", "prompt_id")
            output_path: Path to save the plot (optional)
            figsize: Figure size (width, height)
            perplexity: t-SNE perplexity parameter
            random_state: Random seed for reproducibility
            
        Returns:
            Matplotlib figure object
        """
        # Compute embeddings
        texts = df[text_column].tolist()
        embeddings = self.compute_embeddings(texts)
        
        # Apply t-SNE
        logger.info(f"Computing t-SNE with perplexity={perplexity}")
        tsne = TSNE(
            n_components=2,
            perplexity=perplexity,
            random_state=random_state,
            n_iter=1000
        )
        embeddings_2d = tsne.fit_transform(embeddings)
        
        # Create visualization
        fig, ax = plt.subplots(figsize=figsize)
        
        # Prepare data for plotting
        plot_df = df.copy()
        plot_df['tsne_x'] = embeddings_2d[:, 0]
        plot_df['tsne_y'] = embeddings_2d[:, 1]
        
        # Color mapping
        unique_colors = plot_df[color_by].unique()
        color_palette = sns.color_palette("husl", len(unique_colors))
        color_map = dict(zip(unique_colors, color_palette))
        
        # Marker mapping (if specified)
        if marker_by:
            unique_markers = plot_df[marker_by].unique()
            marker_styles = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']
            marker_map = dict(zip(unique_markers, marker_styles[:len(unique_markers)]))
        else:
            marker_map = None
        
        # Plot each group
        for color_val in unique_colors:
            color_mask = plot_df[color_by] == color_val
            
            if marker_map:
                for marker_val in plot_df[marker_by].unique():
                    mask = color_mask & (plot_df[marker_by] == marker_val)
                    if mask.sum() > 0:
                        ax.scatter(
                            plot_df.loc[mask, 'tsne_x'],
                            plot_df.loc[mask, 'tsne_y'],
                            c=[color_map[color_val]],
                            marker=marker_map[marker_val],
                            s=100,
                            alpha=0.7,
                            edgecolors='black',
                            linewidth=0.5,
                            label=f"{color_val} ({marker_val})"
                        )
            else:
                ax.scatter(
                    plot_df.loc[color_mask, 'tsne_x'],
                    plot_df.loc[color_mask, 'tsne_y'],
                    c=[color_map[color_val]],
                    s=100,
                    alpha=0.7,
                    edgecolors='black',
                    linewidth=0.5,
                    label=color_val
                )
        
        # Styling
        ax.set_xlabel('t-SNE Dimension 1', fontsize=12)
        ax.set_ylabel('t-SNE Dimension 2', fontsize=12)
        ax.set_title(
            f't-SNE Visualization of Response Embeddings\n(colored by {color_by})',
            fontsize=14,
            fontweight='bold'
        )
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save if path provided
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(output_path, dpi=300, bbox_inches='tight')
            logger.info(f"t-SNE plot saved to {output_path}")
        
        return fig
    
    def analyze_clustering(
        self,
        df: pd.DataFrame,
        text_column: str = "response",
        group_by: List[str] = ["language", "model"]
    ) -> pd.DataFrame:
        """
        Analyze clustering patterns by computing within-group and between-group similarities.
        
        Args:
            df: DataFrame containing model responses
            text_column: Column name containing text to analyze
            group_by: Columns to group by for analysis
            
        Returns:
            DataFrame with clustering statistics
        """
        # Compute similarity matrix
        similarity_matrix, df_enhanced = self.calculate_similarity_matrix(df, text_column)
        
        results = []
        
        # For each grouping variable
        for group_col in group_by:
            unique_groups = df[group_col].unique()
            
            for group_val in unique_groups:
                group_mask = (df[group_col] == group_val).values
                
                # Within-group similarity
                within_indices = np.where(group_mask)[0]
                if len(within_indices) > 1:
                    within_pairs = [(i, j) for i in within_indices for j in within_indices if i < j]
                    within_similarities = [similarity_matrix[i, j] for i, j in within_pairs]
                    avg_within = np.mean(within_similarities)
                else:
                    avg_within = np.nan
                
                # Between-group similarity
                between_indices = np.where(~group_mask)[0]
                if len(within_indices) > 0 and len(between_indices) > 0:
                    between_pairs = [(i, j) for i in within_indices for j in between_indices]
                    between_similarities = [similarity_matrix[i, j] for i, j in between_pairs]
                    avg_between = np.mean(between_similarities)
                else:
                    avg_between = np.nan
                
                results.append({
                    "grouping_variable": group_col,
                    "group_value": group_val,
                    "n_samples": group_mask.sum(),
                    "avg_within_similarity": avg_within,
                    "avg_between_similarity": avg_between,
                    "clustering_strength": avg_within - avg_between if not np.isnan(avg_within) and not np.isnan(avg_between) else np.nan
                })
        
        return pd.DataFrame(results)
    
    def compute_correlation(
        self,
        df: pd.DataFrame,
        text_column: str = "response",
        variable1: str = "language",
        variable2: str = "model"
    ) -> Dict[str, float]:
        """
        Compute correlation between categorical variables based on embedding similarity.
        
        Args:
            df: DataFrame containing model responses
            text_column: Column name containing text to analyze
            variable1: First categorical variable
            variable2: Second categorical variable
            
        Returns:
            Dictionary with correlation statistics
        """
        from scipy.stats import pearsonr
        
        # Compute similarity matrix
        similarity_matrix, _ = self.calculate_similarity_matrix(df, text_column)
        
        # Create binary indicators for each variable
        n = len(df)
        
        # Variable 1 similarity (1 if same category, 0 otherwise)
        var1_similarity = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if df.iloc[i][variable1] == df.iloc[j][variable1]:
                    var1_similarity[i, j] = 1
        
        # Variable 2 similarity
        var2_similarity = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if df.iloc[i][variable2] == df.iloc[j][variable2]:
                    var2_similarity[i, j] = 1
        
        # Flatten matrices (excluding diagonal)
        mask = np.triu(np.ones((n, n)), k=1).astype(bool)
        
        embedding_sim_flat = similarity_matrix[mask]
        var1_sim_flat = var1_similarity[mask]
        var2_sim_flat = var2_similarity[mask]
        
        # Calculate correlations
        corr_var1, p_var1 = pearsonr(embedding_sim_flat, var1_sim_flat)
        corr_var2, p_var2 = pearsonr(embedding_sim_flat, var2_sim_flat)
        
        return {
            f"{variable1}_correlation": corr_var1,
            f"{variable1}_p_value": p_var1,
            f"{variable2}_correlation": corr_var2,
            f"{variable2}_p_value": p_var2,
            "stronger_predictor": variable1 if abs(corr_var1) > abs(corr_var2) else variable2
        }
    
    def save_embeddings(
        self,
        df: pd.DataFrame,
        output_path: str,
        text_column: str = "response"
    ):
        """
        Save embeddings to file for later use.
        
        Args:
            df: DataFrame containing responses
            output_path: Path to save embeddings (supports .npy, .npz)
            text_column: Column containing text to embed
        """
        texts = df[text_column].tolist()
        embeddings = self.compute_embeddings(texts)
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if output_path.suffix == '.npy':
            np.save(output_path, embeddings)
        elif output_path.suffix == '.npz':
            # Save with metadata
            np.savez(
                output_path,
                embeddings=embeddings,
                model_name=self.model_name,
                texts=texts
            )
        else:
            raise ValueError(f"Unsupported format: {output_path.suffix}")
        
        logger.info(f"Embeddings saved to {output_path}")


if __name__ == "__main__":
    # Example usage
    
    # Create sample data
    sample_data = pd.DataFrame({
        "response": [
            "The Dai people are an ethnic group in China.",
            "傣族是中国的一个少数民族。",
            "The Dai have strong cultural ties with Thai people.",
            "傣族和泰国人有很强的文化联系。"
        ],
        "language": ["en", "cn", "en", "cn"],
        "model": ["Llama", "Llama", "Qwen", "Qwen"],
        "prompt_id": ["A1", "A1", "B1", "B1"]
    })
    
    # Initialize analyzer
    analyzer = EmbeddingAnalyzer()
    
    # Calculate similarity
    similarity_matrix, df_enhanced = analyzer.calculate_similarity_matrix(sample_data)
    print("Similarity Matrix:")
    print(similarity_matrix)
    
    # Clustering analysis
    clustering_stats = analyzer.analyze_clustering(sample_data)
    print("\nClustering Analysis:")
    print(clustering_stats)
    
    # Correlation analysis
    correlation = analyzer.compute_correlation(sample_data, variable1="language", variable2="model")
    print("\nCorrelation Analysis:")
    print(correlation)
    
    # Visualize t-SNE
    fig = analyzer.visualize_tsne(
        sample_data,
        color_by="language",
        marker_by="model",
        output_path="output/tsne_example.png"
    )
    plt.show()

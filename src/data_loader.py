"""Data loading utilities for movie rating prediction project."""

import os
import pandas as pd
import numpy as np
from typing import Tuple, Optional


class MovieDataLoader:
    """Load and manage movie rating dataset."""
    
    def __init__(self, data_path: str = 'data/raw'):
        """Initialize data loader.
        
        Args:
            data_path: Path to raw data directory
        """
        self.data_path = data_path
        self.df = None
        self.features = None
        self.target = None
    
    def load_data(self, filename: str = 'movies.csv') -> pd.DataFrame:
        """Load movie dataset from CSV file.
        
        Args:
            filename: Name of CSV file to load
            
        Returns:
            Loaded dataframe
        """
        filepath = os.path.join(self.data_path, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        self.df = pd.read_csv(filepath)
        print(f"Loaded data shape: {self.df.shape}")
        print(f"Columns: {list(self.df.columns)}")
        
        return self.df
    
    def get_data_info(self) -> dict:
        """Get basic information about dataset.
        
        Returns:
            Dictionary with dataset info
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        return {
            'shape': self.df.shape,
            'dtypes': self.df.dtypes.to_dict(),
            'missing_values': self.df.isnull().sum().to_dict(),
            'numeric_summary': self.df.describe().to_dict()
        }
    
    def get_features_and_target(
        self, target_col: str = 'rating'
    ) -> Tuple[pd.DataFrame, pd.Series]:
        """Separate features and target variable.
        
        Args:
            target_col: Name of target column
            
        Returns:
            Tuple of features dataframe and target series
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        if target_col not in self.df.columns:
            raise ValueError(f"Target column '{target_col}' not found in data")
        
        self.target = self.df[target_col]
        self.features = self.df.drop(columns=[target_col])
        
        return self.features, self.target


if __name__ == '__main__':
    # Example usage
    loader = MovieDataLoader()
    df = loader.load_data()
    print(loader.get_data_info())

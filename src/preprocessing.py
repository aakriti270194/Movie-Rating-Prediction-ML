"""Data preprocessing utilities for movie rating prediction."""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from typing import List, Optional


class DataPreprocessor:
    """Handle data cleaning and preprocessing tasks."""
    
    def __init__(self):
        """Initialize preprocessor."""
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='mean')
        self.label_encoders = {}
    
    def handle_missing_values(self, df: pd.DataFrame, strategy: str = 'mean') -> pd.DataFrame:
        """Handle missing values in dataset."""
        df_copy = df.copy()
        print(f"Missing values before: {df_copy.isnull().sum().sum()}")
        
        if strategy == 'mean':
            df_copy = df_copy.fillna(df_copy.mean())
        elif strategy == 'median':
            df_copy = df_copy.fillna(df_copy.median())
        
        print(f"Missing values after: {df_copy.isnull().sum().sum()}")
        return df_copy
    
    def remove_outliers(self, df: pd.DataFrame, columns: List[str], method: str = 'iqr') -> pd.DataFrame:
        """Remove outliers from dataset using IQR method."""
        df_copy = df.copy()
        initial_shape = df_copy.shape[0]
        
        for col in columns:
            Q1 = df_copy[col].quantile(0.25)
            Q3 = df_copy[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df_copy = df_copy[(df_copy[col] >= lower) & (df_copy[col] <= upper)]
        
        print(f"Rows removed: {initial_shape - df_copy.shape[0]}")
        return df_copy
    
    def encode_categorical(self, df: pd.DataFrame, categorical_cols: List[str]) -> pd.DataFrame:
        """Encode categorical variables."""
        df_copy = df.copy()
        
        for col in categorical_cols:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
                df_copy[col] = self.label_encoders[col].fit_transform(df_copy[col])
            else:
                df_copy[col] = self.label_encoders[col].transform(df_copy[col])
        
        return df_copy
    
    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Scale numeric features using StandardScaler."""
        df_copy = df.copy()
        numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
        df_copy[numeric_cols] = self.scaler.fit_transform(df_copy[numeric_cols])
        return df_copy

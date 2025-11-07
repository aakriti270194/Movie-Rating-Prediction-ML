"""Utility functions for movie rating prediction."""

import numpy as np
import pandas as pd
from typing import Tuple


def train_test_split(
    X: np.ndarray, y: np.ndarray, test_size: float = 0.2, random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Split data into train and test sets."""
    np.random.seed(random_state)
    n = len(X)
    n_test = int(n * test_size)
    indices = np.random.permutation(n)
    test_idx = indices[:n_test]
    train_idx = indices[n_test:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


def normalize(X: np.ndarray) -> np.ndarray:
    """Normalize features to 0-1 range."""
    X_min = X.min(axis=0)
    X_max = X.max(axis=0)
    return (X - X_min) / (X_max - X_min + 1e-8)


def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """Calculate evaluation metrics for regression."""
    mse = np.mean((y_true - y_pred) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_true - y_pred))
    r2 = 1 - (np.sum((y_true - y_pred) ** 2) / np.sum((y_true - y_true.mean()) ** 2))
    return {'mse': mse, 'rmse': rmse, 'mae': mae, 'r2': r2}


def save_model(model, filepath: str) -> None:
    """Save trained model to file."""
    import pickle
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)


def load_model(filepath: str):
    """Load trained model from file."""
    import pickle
    with open(filepath, 'rb') as f:
        return pickle.load(f)

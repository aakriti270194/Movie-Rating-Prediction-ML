"""Model Evaluator Module

This module provides comprehensive evaluation metrics and visualization tools
for assessing the performance of machine learning models in the movie rating
prediction project.

Author: Aakriti
Date: 2025-11-11
"""

import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    median_absolute_error,
    mean_absolute_percentage_error
)


class ModelEvaluator:
    """Comprehensive model evaluation class for regression tasks."""

    def __init__(self):
        """Initialize the ModelEvaluator."""
        self.metrics = {}
        self.predictions = None
        self.actual_values = None

    def evaluate(self, y_true, y_pred):
        """Calculate comprehensive evaluation metrics.

        Parameters
        ----------
        y_true : array-like
            True values
        y_pred : array-like
            Predicted values

        Returns
        -------
        dict
            Dictionary containing all calculated metrics
        """
        self.predictions = y_pred
        self.actual_values = y_true

        # Calculate metrics
        self.metrics['MAE'] = mean_absolute_error(y_true, y_pred)
        self.metrics['RMSE'] = np.sqrt(mean_squared_error(y_true, y_pred))
        self.metrics['R2'] = r2_score(y_true, y_pred)
        self.metrics['Median_AE'] = median_absolute_error(y_true, y_pred)
        self.metrics['MAPE'] = mean_absolute_percentage_error(y_true, y_pred)

        return self.metrics

    def print_report(self):
        """Print a formatted evaluation report."""
        if not self.metrics:
            print("No metrics calculated yet. Call evaluate() first.")
            return

        print("\n" + "="*50)
        print("MODEL EVALUATION REPORT")
        print("="*50)
        for metric, value in self.metrics.items():
            print(f"{metric:.<20} {value:.4f}")
        print("="*50 + "\n")

    def get_metrics_dataframe(self):
        """Return metrics as a pandas DataFrame.

        Returns
        -------
        pd.DataFrame
            DataFrame with metrics
        """
        return pd.DataFrame(self.metrics, index=[0]).T

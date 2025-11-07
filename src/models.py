"""Machine learning models for movie rating prediction."""

import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from typing import Dict


class MovieRatingPredictor:
    """Main predictor class for movie ratings using multiple algorithms."""
    
    def __init__(self):
        """Initialize predictor with different models."""
        self.models = {
            'linear': LinearRegression(),
            'ridge': Ridge(alpha=1.0),
            'lasso': Lasso(alpha=0.1),
            'rf': RandomForestRegressor(n_estimators=100, random_state=42),
            'gb': GradientBoostingRegressor(n_estimators=100, random_state=42)
        }
        self.best_model = None
        self.best_score = None
        self.trained_models = {}
    
    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        """Train all models."""
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            self.trained_models[name] = model
    
    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> Dict:
        """Evaluate all trained models."""
        results = {}
        
        for name, model in self.trained_models.items():
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            mae = mean_absolute_error(y_test, y_pred)
            
            results[name] = {'r2': r2, 'rmse': rmse, 'mae': mae}
            
            if self.best_score is None or r2 > self.best_score:
                self.best_score = r2
                self.best_model = model
        
        return results
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions using best model."""
        if self.best_model is None:
            raise ValueError("Model not trained yet")
        return self.best_model.predict(X)

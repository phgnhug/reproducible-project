"""Model evaluation module for House Price Prediction project."""
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


class ModelEvaluator:
    """Evaluate model performance for house price prediction."""

    @staticmethod
    def calculate_rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Calculate Root Mean Squared Error."""
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        return rmse

    @staticmethod
    def calculate_rmse_log(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Calculate RMSE on log scale."""
        rmse_log = np.sqrt(np.mean((np.log(y_true) - np.log(y_pred)) ** 2))
        return rmse_log

    @staticmethod
    def calculate_mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Calculate Mean Absolute Error."""
        mae = mean_absolute_error(y_true, y_pred)
        return mae

    @staticmethod
    def calculate_r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Calculate R-squared score."""
        r2 = r2_score(y_true, y_pred)
        return r2

    @staticmethod
    def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray, name: str = "Model") -> dict:
        """Comprehensive model evaluation."""
        metrics = {
            "RMSE": ModelEvaluator.calculate_rmse(y_true, y_pred),
            "RMSE_Log": ModelEvaluator.calculate_rmse_log(y_true, y_pred),
            "MAE": ModelEvaluator.calculate_mae(y_true, y_pred),
            "R2": ModelEvaluator.calculate_r2(y_true, y_pred),
        }

        print(f"\n{'='*60}")
        print(f"EVALUATION METRICS - {name}")
        print(f"{'='*60}")
        print(f"RMSE:             {metrics['RMSE']:>12.4f}")
        print(f"RMSE (log):       {metrics['RMSE_Log']:>12.4f}")
        print(f"MAE:              {metrics['MAE']:>12.4f}")
        print(f"R² Score:         {metrics['R2']:>12.4f}")
        print(f"{'='*60}\n")
        return metrics

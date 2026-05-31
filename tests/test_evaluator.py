"""Tests for the ModelEvaluator class."""
import numpy as np
import pytest

from house_price_predictor.models.evaluator import ModelEvaluator


@pytest.fixture
def sample_predictions():
    """Sample true and predicted values."""
    y_true = np.array([200000, 150000, 300000, 120000, 250000])
    y_pred = np.array([210000, 145000, 290000, 125000, 260000])
    return y_true, y_pred


def test_calculate_rmse(sample_predictions):
    """RMSE should be a positive float."""
    y_true, y_pred = sample_predictions
    rmse = ModelEvaluator.calculate_rmse(y_true, y_pred)
    assert isinstance(rmse, float)
    assert rmse > 0


def test_calculate_mae(sample_predictions):
    """MAE should be less than or equal to RMSE."""
    y_true, y_pred = sample_predictions
    mae = ModelEvaluator.calculate_mae(y_true, y_pred)
    rmse = ModelEvaluator.calculate_rmse(y_true, y_pred)
    assert mae <= rmse


def test_calculate_r2_perfect(sample_predictions):
    """R² should be 1.0 for perfect predictions."""
    y_true, _ = sample_predictions
    r2 = ModelEvaluator.calculate_r2(y_true, y_true)
    assert r2 == pytest.approx(1.0)


def test_calculate_r2_range(sample_predictions):
    """R² should be between -inf and 1."""
    y_true, y_pred = sample_predictions
    r2 = ModelEvaluator.calculate_r2(y_true, y_pred)
    assert r2 <= 1.0


def test_evaluate_model_returns_all_metrics(sample_predictions):
    """evaluate_model should return all four metrics."""
    y_true, y_pred = sample_predictions
    metrics = ModelEvaluator.evaluate_model(y_true, y_pred, name="Test")
    assert "RMSE" in metrics
    assert "RMSE_Log" in metrics
    assert "MAE" in metrics
    assert "R2" in metrics


def test_rmse_log_positive(sample_predictions):
    """RMSE log should be positive."""
    y_true, y_pred = sample_predictions
    rmse_log = ModelEvaluator.calculate_rmse_log(y_true, y_pred)
    assert rmse_log > 0

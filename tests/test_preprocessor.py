"""Tests for the DataPreprocessor class."""
import numpy as np
import pandas as pd
import pytest

from house_price_predictor.data.preprocessor import DataPreprocessor


@pytest.fixture
def sample_data():
    """Create sample dataset for testing."""
    return pd.DataFrame({
        "Id": [1, 2, 3, 4, 5, 6],
        "GrLivArea": [1500, 1200, 5000, 800, 2000, 1800],
        "Neighborhood": ["NAmes", None, "OldTown", "NAmes", None, "OldTown"],
        "LotArea": [8450, 9600, None, 7200, 11250, 9550],
        "SalePrice": [200000, 150000, 300000, 120000, 250000, 180000],
        "isTrain": [1, 1, 1, 1, 1, 1],
    })


def test_handle_missing_values_categorical(sample_data):
    """Missing categorical values should be filled with 'None'."""
    preprocessor = DataPreprocessor(sample_data)
    result = preprocessor.handle_missing_values()
    assert result["Neighborhood"].isnull().sum() == 0
    assert "None" in result["Neighborhood"].values


def test_handle_missing_values_numeric(sample_data):
    """Missing numeric values should be filled with column mean."""
    preprocessor = DataPreprocessor(sample_data)
    result = preprocessor.handle_missing_values()
    assert result["LotArea"].isnull().sum() == 0


def test_remove_outliers(sample_data):
    """Rows with GrLivArea > 4000 should be removed."""
    preprocessor = DataPreprocessor(sample_data)
    result = preprocessor.remove_outliers()
    assert result["GrLivArea"].max() <= 4000
    assert len(result) == 5


def test_encode_categorical(sample_data):
    """Categorical columns should be encoded as integers."""
    preprocessor = DataPreprocessor(sample_data)
    preprocessor.handle_missing_values()
    result = preprocessor.encode_categorical()
    assert result["Neighborhood"].dtype in [np.int32, np.int64, np.int8]


def test_transform_skewed_features(sample_data):
    """Skewed numeric features should be log-transformed."""
    preprocessor = DataPreprocessor(sample_data)
    original_max = sample_data["LotArea"].max()
    preprocessor.handle_missing_values()
    result = preprocessor.transform_skewed_features(threshold=0.0)
    assert result["LotArea"].max() < original_max

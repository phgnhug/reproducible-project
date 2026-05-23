"""Data loading module for House Price Prediction project."""
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple


class DataLoader:
    """Load and combine train/test data for house price prediction."""

    def __init__(self, data_dir: str = "data/raw"):
        self.data_dir = Path(data_dir)
        self.train = None
        self.test = None
        self.combined = None

    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Load train and test datasets from CSV files."""
        train_path = self.data_dir / "train.csv"
        test_path = self.data_dir / "test.csv"

        if not train_path.exists():
            raise FileNotFoundError(f"Training data not found at {train_path}")
        if not test_path.exists():
            raise FileNotFoundError(f"Test data not found at {test_path}")

        print(f"Loading training data from {train_path}...")
        self.train = pd.read_csv(train_path)
        print(f"Loading test data from {test_path}...")
        self.test = pd.read_csv(test_path)

        print(f"\n✓ Train shape: {self.train.shape}")
        print(f"✓ Test shape: {self.test.shape}")
        return self.train, self.test

    def combine_datasets(self) -> pd.DataFrame:
        """Combine train and test datasets for preprocessing."""
        if self.train is None or self.test is None:
            raise ValueError("Load data first using load_data()")

        self.test["SalePrice"] = np.nan
        self.train["isTrain"] = 1
        self.test["isTrain"] = 0
        self.combined = pd.concat([self.train, self.test], ignore_index=True)

        print(f"\n✓ Combined dataset shape: {self.combined.shape}")
        return self.combined

    def get_data_info(self) -> dict:
        """Get summary information about the datasets."""
        if self.train is None:
            raise ValueError("Load data first using load_data()")

        info = {
            "train_rows": len(self.train),
            "test_rows": len(self.test),
            "n_features": len(self.train.columns),
            "n_categorical": len(self.train.select_dtypes(include=["object"]).columns),
            "n_numeric": len(self.train.select_dtypes(include=[np.number]).columns),
        }

        print("\n" + "="*60)
        print("DATA SUMMARY")
        print("="*60)
        print(f"Train samples:        {info['train_rows']}")
        print(f"Test samples:         {info['test_rows']}")
        print(f"Total features:       {info['n_features']}")
        print(f"  - Categorical:      {info['n_categorical']}")
        print(f"  - Numeric:          {info['n_numeric']}")
        print("="*60 + "\n")
        return info

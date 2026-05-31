"""Data preprocessing module for House Price Prediction project."""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from scipy.stats import skew
from typing import Tuple


class DataPreprocessor:
    """Preprocess and engineer features for house price prediction."""

    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
        self.categorical_cols = []
        self.numeric_cols = []
        self.label_encoders = {}

    def handle_missing_values(self) -> pd.DataFrame:
        """Handle missing values in the dataset."""
        print("Handling missing values...")
        categorical = self.data.select_dtypes(include=["object", "str"]).columns
        numeric = self.data.select_dtypes(include=[np.number]).columns

        for col in categorical:
            if self.data[col].isnull().any():
                self.data[col] = self.data[col].fillna("None")
                print(f"  ✓ {col}: Filled with 'None'")

        for col in numeric:
            if col != "SalePrice" and self.data[col].isnull().any():
                fill_value = self.data[col].mean()
                self.data[col] = self.data[col].fillna(fill_value)
                print(f"  ✓ {col}: Filled with mean ({fill_value:.2f})")
        print()
        return self.data

    def remove_outliers(self) -> pd.DataFrame:
        """Remove outliers from the dataset."""
        print("Removing outliers...")
        initial_rows = len(self.data)

        if "GrLivArea" in self.data.columns:
            self.data = self.data[self.data["GrLivArea"] <= 4000]
            removed = initial_rows - len(self.data)
            print(f"  ✓ Removed {removed} rows with GrLivArea > 4000")
        print()
        return self.data

    def encode_categorical(self) -> pd.DataFrame:
        """Encode categorical variables."""
        print("Encoding categorical variables...")
        categorical = self.data.select_dtypes(include=["object", "str"]).columns
        self.categorical_cols = list(categorical)

        for col in categorical:
            if col not in self.label_encoders:
                le = LabelEncoder()
                self.data[col] = le.fit_transform(self.data[col].astype(str))
                self.label_encoders[col] = le
                print(f"  ✓ {col}: Encoded ({len(le.classes_)} classes)")
        print()
        return self.data

    def transform_skewed_features(self, threshold: float = 0.75) -> pd.DataFrame:
        """Transform skewed features using log(x+1) transformation."""
        print(f"Transforming skewed features (threshold={threshold})...")
        numeric = self.data.select_dtypes(include=[np.number]).columns

        for col in numeric:
            if col == "SalePrice":
                continue
            skewness_val = skew(self.data[col].dropna())
            if abs(skewness_val) > threshold:
                self.data[col] = np.log1p(self.data[col])
                print(f"  ✓ {col}: Log transformed (skewness={skewness_val:.2f})")
        print()
        return self.data

    def create_train_validation_split(
        self, test_size: float = 0.25, random_state: int = 123
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Split training data into train and validation sets."""
        from sklearn.model_selection import train_test_split

        print("Creating train/validation split...")
        train = self.data[self.data["isTrain"] == 1].copy()
        test = self.data[self.data["isTrain"] == 0].copy()

        train_X = train.drop(["Id", "isTrain", "SalePrice"], axis=1)
        train_y = train["SalePrice"]

        X_train, X_val, y_train, y_val = train_test_split(
            train_X, train_y, test_size=test_size, random_state=random_state
        )

        train_split = X_train.copy()
        train_split["SalePrice"] = y_train
        val_split = X_val.copy()
        val_split["SalePrice"] = y_val
        test_split = test.drop(["Id", "isTrain"], axis=1)

        print(f"  ✓ Train set: {len(train_split)} samples")
        print(f"  ✓ Validation set: {len(val_split)} samples")
        print(f"  ✓ Test set: {len(test_split)} samples")
        print()
        return train_split, val_split, test_split

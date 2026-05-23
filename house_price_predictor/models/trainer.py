"""Model training module for House Price Prediction project."""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


class ModelTrainer:
    """Train Random Forest model for house price prediction."""

    def __init__(self, random_state: int = 123):
        self.random_state = random_state
        self.model = None
        self.feature_names = None

    def train_random_forest(self, X_train: pd.DataFrame, y_train: pd.Series, n_estimators: int = 100):
        """Train Random Forest model."""
        print("Training Random Forest model...")
        print(f"  Features: {len(X_train.columns)}")
        print(f"  Samples: {len(X_train)}")
        print(f"  Trees: {n_estimators}\n")

        self.feature_names = X_train.columns.tolist()
        self.model = RandomForestRegressor(
            n_estimators=n_estimators,
            random_state=self.random_state,
            n_jobs=-1,
            verbose=1
        )
        self.model.fit(X_train, y_train)
        print("✓ Model training completed!\n")
        return self.model

    def get_feature_importance(self, top_n: int = 20) -> pd.DataFrame:
        """Get feature importance from trained model."""
        if self.model is None:
            raise ValueError("Train model first using train_random_forest()")

        importances = self.model.feature_importances_
        feature_importance_df = pd.DataFrame({
            "Feature": self.feature_names,
            "Importance": importances
        }).sort_values("Importance", ascending=False)

        print(f"\nTop {top_n} Important Features:")
        print("="*50)
        print(feature_importance_df.head(top_n).to_string(index=False))
        print("="*50 + "\n")
        return feature_importance_df

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Make predictions using trained model."""
        if self.model is None:
            raise ValueError("Train model first using train_random_forest()")
        return self.model.predict(X)

    def save_model(self, filepath: str) -> None:
        """Save trained model to file."""
        import joblib
        if self.model is None:
            raise ValueError("Train model first before saving")
        joblib.dump(self.model, filepath)
        print(f"✓ Model saved to {filepath}\n")

    def load_model(self, filepath: str) -> None:
        """Load trained model from file."""
        import joblib
        self.model = joblib.load(filepath)
        print(f"✓ Model loaded from {filepath}\n")

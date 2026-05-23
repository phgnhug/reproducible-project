#!/usr/bin/env python3
"""Quick test of the full pipeline"""
import sys
from house_price_predictor.data.loader import DataLoader
from house_price_predictor.data.preprocessor import DataPreprocessor
from house_price_predictor.models.trainer import ModelTrainer
from house_price_predictor.models.evaluator import ModelEvaluator

try:
    print("=" * 60)
    print("TESTING FULL PIPELINE")
    print("=" * 60)
    
    # Load data
    print("\n1️⃣ Loading data...")
    loader = DataLoader(data_dir='data/raw')
    train, test = loader.load_data()
    loader.get_data_info()
    
    # Combine
    print("\n2️⃣ Combining datasets...")
    combined = loader.combine_datasets()
    
    # Preprocess
    print("\n3️⃣ Preprocessing...")
    preprocessor = DataPreprocessor(combined)
    preprocessor.handle_missing_values()
    preprocessor.remove_outliers()
    preprocessor.encode_categorical()
    preprocessor.transform_skewed_features()
    train_split, val_split, test_split = preprocessor.create_train_validation_split()
    
    # Train
    print("\n4️⃣ Training model...")
    X_train = train_split.drop('SalePrice', axis=1)
    y_train = train_split['SalePrice']
    X_val = val_split.drop('SalePrice', axis=1)
    y_val = val_split['SalePrice']
    
    trainer = ModelTrainer()
    trainer.train_random_forest(X_train, y_train, n_estimators=50)
    
    # Evaluate
    print("\n5️⃣ Evaluating...")
    train_pred = trainer.predict(X_train)
    val_pred = trainer.predict(X_val)
    
    ModelEvaluator.evaluate_model(y_train, train_pred, name="Train")
    ModelEvaluator.evaluate_model(y_val, val_pred, name="Validation")
    
    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

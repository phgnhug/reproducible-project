# House Price Prediction - Reproducible Research Project

Translating R Kaggle analysis to Python with reproducibility best practices.

## Quick Start

```bash
# Pull Docker image
docker pull phgnhug/house-price-predictor:latest

# Run pipeline
docker run -it phgnhug/house-price-predictor:latest bash -c "python3 test_pipeline.py"

# Expected output:
# ✅ ALL TESTS PASSED!
# VALIDATION R²: 0.8683
```

## Results
- Training R²: 0.9813
- Validation R²: 0.8683
- Model: Random Forest (50 trees)

## GitHub
https://github.com/phgnhug/reproducible-project

## Team
- Nhung Nguyen (data loading)
- Chau Phan (preprocessing)
- Sherry (model training)

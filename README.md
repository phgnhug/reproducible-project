# House Price Prediction - Reproducible Research Project

**Translating from R to Python with Reproducible Research Best Practices**

## Project Overview

This project reproduces a house price prediction analysis from Kaggle, translating code from R to Python while implementing reproducible research principles.

**Original Source:** [Predicting House Prices using R](https://www.kaggle.com/code/pradeeptripathi/predicting-house-prices-using-r)

**Dataset:** [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

## Project Goals

 Translate R code to Python  
 Reproduce original results  
 Implement reproducible research practices  
 Use proper software engineering practices  
 Document all steps clearly  

## Dataset

- **Training samples:** 1,460 houses
- **Test samples:** 1,459 houses
- **Features:** 79 (43 categorical, 38 numerical)
- **Target:** SalePrice (continuous)
- **Location:** Ames, Iowa

## Project Structure
## Quick Start

### Prerequisites

- Python 3.11+
- Git

### Installation

```bash
git clone https://github.com/phgnhug/reproducible-project.git
cd reproducible-project
python3 -m venv env
source env/bin/activate
make install
```

### Download Data

1. Download from [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
2. Place `train.csv` and `test.csv` in `data/raw/`

## Team Roles

| Person | Role | Files |
|--------|------|-------|
| A | Data Loading & EDA | `house_price_predictor/data/loader.py`, `notebooks/01_exploration.ipynb` |
| B | Preprocessing & Feature Engineering | `house_price_predictor/data/preprocessor.py`, `notebooks/02_preprocessing.ipynb` |
| C | Model Training & Evaluation | `house_price_predictor/models/trainer.py`, `house_price_predictor/models/evaluator.py` |

## Commands

```bash
make install       # Install dependencies
make dev           # Install dev dependencies
make format        # Format code
make lint          # Check code quality
make test          # Run tests
make docker-build  # Build Docker image
make docker-run    # Run in Docker
```

## References

- Original R notebook: [Predicting House Prices using R](https://www.kaggle.com/code/pradeeptripathi/predicting-house-prices-using-r)
- Dataset: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

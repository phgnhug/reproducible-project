# House Price Prediction — Reproducible Research Project

Translating an R Kaggle house price analysis to Python with reproducibility best practices.

## Team

| Name | Contribution |
|---|---|
| Nhung Nguyen | Data loading module |
| Chau Phan | Preprocessing module |
| Sherry | Model training module |

---

## Quick Start (Presentation)

```bash
# 1. Clone the repo
git clone https://github.com/phgnhug/reproducible-project.git
cd reproducible-project

# 2. Generate report
docker compose run --rm report

# 3. Open the report
open report/final_report.html        # Mac
start report\final_report.html       # Windows
```

---

## Alternative (if docker compose fails)

**Mac/Linux:**
```bash
docker run --rm -v $(pwd)/report:/app/report phgnhug/house-price-predictor:latest make report
```

**Windows PowerShell:**
```bash
docker run --rm -v ${PWD}/report:/app/report phgnhug/house-price-predictor:latest make report
```

**Windows Command Prompt:**
```bash
docker run --rm -v %cd%/report:/app/report phgnhug/house-price-predictor:latest make report
```

---

## Makefile Commands

```bash
make install      # Install production dependencies
make dev          # Install all dependencies
make lint         # Run flake8
make format       # Run black + isort
make test         # Run pytest with coverage
make report       # Render Quarto report
make docs         # Build Sphinx docs
make docker-build # Build Docker image
make docker-push  # Push to DockerHub
```

---

## Results

| Metric | Value |
|---|---|
| Model | Random Forest (50 trees) |
| Training R² | 0.9813 |
| Validation R² | 0.8683 |

---

## AI Usage Disclosure

This project used **Claude Sonnet** (Anthropic) to assist with package structure, docstrings, Sphinx/Quarto configuration, and README. All pipeline logic and results are the team's own work.

# Quick Start for Presentation

## Prerequisites
- Docker installed

## Run the Project & Generate Report

```bash
# Step 1: Pull image from DockerHub
docker pull phgnhug/house-price-predictor:latest

# Step 2: Create output folder
mkdir -p output

# Step 3: Run pipeline and generate report
docker run -v $(pwd)/output:/app/output phgnhug/house-price-predictor:latest bash -c "python3 test_pipeline.py && quarto render report/final_report.qmd -o /app/output/report.html"

# Step 4: View the report
open output/report.html
```

The report will show:
- Dataset overview
- Preprocessing steps
- Model results (R² = 0.8683)
- Feature importance
- Conclusions
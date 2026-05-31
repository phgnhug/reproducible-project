.PHONY: help install dev lint format test clean report docs docker-build docker-push docker-run

help:
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make dev          - Install all dependencies including dev tools"
	@echo "  make lint         - Run linting (flake8)"
	@echo "  make format       - Format code (black, isort)"
	@echo "  make test         - Run tests with coverage"
	@echo "  make report       - Generate Quarto HTML report"
	@echo "  make docs         - Generate Sphinx HTML documentation"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make docker-build - Build Docker image locally"
	@echo "  make docker-push  - Push image to DockerHub"
	@echo "  make docker-run   - Run container and generate report"

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e ".[dev]"

lint:
	flake8 house_price_predictor tests

format:
	black house_price_predictor tests
	isort house_price_predictor tests

test:
	pytest tests/ -v --cov=house_price_predictor --cov-report=term-missing

report:
	quarto render report/final_report.qmd --to html
	@echo "Report generated: report/final_report.html"

docs:
	cd docs && sphinx-apidoc -o source ../house_price_predictor --force
	cd docs && make html
	@echo "Documentation: docs/build/html/index.html"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info
	rm -rf .coverage htmlcov/
	rm -rf docs/build/

docker-build:
	docker build -t phgnhug/house-price-predictor:latest .

docker-push:
	docker push phgnhug/house-price-predictor:latest

docker-run:
	docker run --rm \
		-v $(PWD)/report:/app/report \
		phgnhug/house-price-predictor:latest \
		make report

.DEFAULT_GOAL := help

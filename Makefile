.PHONY: help install dev lint format test clean docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make dev          - Install development dependencies"
	@echo "  make lint         - Run linting (flake8)"
	@echo "  make format       - Format code (black, isort)"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-run   - Run Docker container"

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
	pytest tests/ -v --cov=house_price_predictor

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info
	rm -rf .coverage htmlcov/

docker-build:
	docker build -t house-price-predictor:latest .

docker-run:
	docker run -it -v $(PWD)/data:/app/data house-price-predictor:latest

.DEFAULT_GOAL := help

PYTHON ?= python3.12
VENV   := .venv
BIN    := $(VENV)/bin
# Same data root as src/off_pipeline/config.py (environment variables are visible to make)
OFF_DATA_DIR ?= data

.PHONY: install sample bronze silver gold test lint fmt clean

install:  ## Create the virtualenv and install the project in editable mode
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev]"

sample:   ## Download a sample of the Open Food Facts CSV (default 50k rows)
	$(BIN)/python scripts/download_sample.py --rows $${ROWS:-50000}

bronze:   ## Run the bronze ingestion job
	$(BIN)/python -m off_pipeline.bronze.ingest

silver:   ## Run the silver job
	$(BIN)/python -m off_pipeline.silver.products

gold:     ## Run the gold job
	$(BIN)/python -m off_pipeline.gold.star_schema

test:
	$(BIN)/pytest

lint:
	$(BIN)/ruff check src tests scripts
	$(BIN)/ruff format --check src tests scripts

fmt:
	$(BIN)/ruff check --fix src tests scripts
	$(BIN)/ruff format src tests scripts

clean:    ## Remove local lakehouse tables (keeps the raw sample)
	rm -rf "$(OFF_DATA_DIR)/lakehouse" spark-warehouse metastore_db derby.log

"""Central place for paths and table locations.

Everything lives under ``OFF_DATA_DIR`` (default: ``./data``) so the same code can later point
at cloud storage (ADLS, S3) by changing a single environment variable.
"""

import os
from pathlib import Path

DATA_DIR = Path(os.environ.get("OFF_DATA_DIR", Path(__file__).resolve().parents[2] / "data"))

RAW_DIR = DATA_DIR / "raw"
LAKEHOUSE_DIR = DATA_DIR / "lakehouse"

BRONZE_DIR = LAKEHOUSE_DIR / "bronze"
SILVER_DIR = LAKEHOUSE_DIR / "silver"
GOLD_DIR = LAKEHOUSE_DIR / "gold"

SAMPLE_CSV = RAW_DIR / "products_sample.csv"

# Table paths
BRONZE_PRODUCTS = BRONZE_DIR / "products"
SILVER_PRODUCTS = SILVER_DIR / "products"
GOLD_DIM_PRODUCT = GOLD_DIR / "dim_product"
GOLD_DIM_BRAND = GOLD_DIR / "dim_brand"
GOLD_DIM_CATEGORY = GOLD_DIR / "dim_category"
GOLD_DIM_COUNTRY = GOLD_DIR / "dim_country"
GOLD_FACT_NUTRITION = GOLD_DIR / "fact_nutrition"

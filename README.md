# openfoodfacts-data-pipeline

Lakehouse pipeline on [Open Food Facts](https://world.openfoodfacts.org/) data, built with
**PySpark** and **Delta Lake**, following a **medallion architecture** (bronze / silver / gold).

> Work in progress — see [ROADMAP.md](ROADMAP.md) for what is done and what is next.

## Architecture

```
Open Food Facts CSV export
        │  scripts/download_sample.py
        ▼
data/raw/products_sample.csv
        │  bronze/ingest.py     raw, all strings, + ingestion metadata, append-only
        ▼
bronze.products (Delta)
        │  silver/products.py   typed, cleaned, deduplicated, SCD2 history via MERGE
        ▼
silver.products (Delta)
        │  gold/star_schema.py  star schema for analytics
        ▼
gold.fact_nutrition + dim_product / dim_brand / dim_category / dim_country (Delta)
```

Data quality checks (`quality/checks.py`) run between layers and fail the job above a threshold.

## Stack

| Concern        | Choice                                  |
|----------------|-----------------------------------------|
| Processing     | PySpark 4.0                             |
| Storage format | Delta Lake 4.0 (ACID, MERGE, time travel) |
| Tests          | pytest + chispa                         |
| Lint / format  | ruff                                    |
| CI             | GitHub Actions                          |

## Getting started

Requirements: Python 3.10–3.12 and Java 17 or 21 (`java -version`).

```bash
make install          # virtualenv + dependencies
make sample           # first 50k rows of the OFF export → data/raw/ (ROWS=200000 make sample for more)
make test             # includes a Delta smoke test
```

Then run the layers once they are implemented:

```bash
make bronze
make silver
make gold
```

## Project layout

```
src/off_pipeline/
  config.py        paths of every table (override root with OFF_DATA_DIR)
  spark.py         SparkSession with Delta enabled
  bronze/ silver/ gold/   one module per layer
  quality/         reusable data quality checks
scripts/           utilities (sample download)
notebooks/         exploration only — production logic lives in src/
tests/unit         pure transformation tests on tiny DataFrames
tests/integration  tests that write real Delta tables
```

## Data license

Open Food Facts data is available under the
[Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/1-0/).

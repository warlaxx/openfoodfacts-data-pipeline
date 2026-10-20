"""Bronze layer: land the raw Open Food Facts CSV into a Delta table, as-is.

TODO (à écrire toi-même) :
- Lire ``SAMPLE_CSV`` (séparateur tabulation, en-tête, tout en string : pas d'inférence de schéma).
- Ajouter des colonnes techniques : ``_ingested_at``, ``_source_file``, ``_batch_id``.
- Écrire en Delta dans ``BRONZE_PRODUCTS`` (mode append : le bronze garde tout l'historique).
- Bonus semaine 4 : chargement incrémental (ne réingérer que les lignes dont
  ``last_modified_t`` est postérieur au dernier batch).
"""

from pyspark.sql import DataFrame, SparkSession

from off_pipeline import config
from off_pipeline.spark import get_spark


def read_raw(spark: SparkSession, path: str) -> DataFrame:
    raise NotImplementedError("À toi de jouer : lecture du CSV brut")


def add_ingestion_metadata(df: DataFrame, source_file: str, batch_id: str) -> DataFrame:
    raise NotImplementedError("À toi de jouer : colonnes techniques")


def run() -> None:
    spark = get_spark("off-bronze")
    df = read_raw(spark, str(config.SAMPLE_CSV))
    # ...
    _ = df


if __name__ == "__main__":
    run()

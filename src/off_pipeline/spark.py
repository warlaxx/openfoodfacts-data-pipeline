"""SparkSession factory with Delta Lake enabled."""

import os
import sys

from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession


def get_spark(app_name: str = "off-pipeline", master: str = "local[*]") -> SparkSession:
    """Return a local SparkSession configured for Delta Lake.

    ``configure_spark_with_delta_pip`` adds the Delta jars matching the installed
    ``delta-spark`` package, so no manual jar download is needed.
    """
    # Python workers must run the same interpreter as the driver (the venv), not the
    # system ``python3``, otherwise PySpark fails with PYTHON_VERSION_MISMATCH.
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    builder = (
        SparkSession.builder.appName(app_name)
        .master(master)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        # Small local machine: avoid 200 shuffle partitions for a few MB of data.
        .config("spark.sql.shuffle.partitions", "8")
        .config("spark.ui.showConsoleProgress", "false")
    )
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    return spark

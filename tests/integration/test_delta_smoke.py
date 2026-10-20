"""Smoke test: Spark starts, Delta writes, reads, and keeps versions."""

import pytest

pytestmark = pytest.mark.integration


def test_delta_roundtrip_and_time_travel(spark, tmp_path):
    path = str(tmp_path / "smoke")

    spark.createDataFrame([("3017620422003", "Nutella")], ["code", "product_name"]).write.format(
        "delta"
    ).save(path)
    spark.createDataFrame([("5449000000996", "Coca-Cola")], ["code", "product_name"]).write.format(
        "delta"
    ).mode("append").save(path)

    assert spark.read.format("delta").load(path).count() == 2
    assert spark.read.format("delta").option("versionAsOf", 0).load(path).count() == 1

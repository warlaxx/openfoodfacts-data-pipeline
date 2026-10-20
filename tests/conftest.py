import pytest

from off_pipeline.spark import get_spark


@pytest.fixture(scope="session")
def spark():
    """One local SparkSession (with Delta) shared by the whole test run."""
    session = get_spark("off-pipeline-tests", master="local[2]")
    yield session
    session.stop()

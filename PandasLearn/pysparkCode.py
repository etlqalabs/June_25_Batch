import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder \
        .appName("ETLTesting") \
        .master("local[*]") \
        .getOrCreate()

def test_compare_dataframes(spark):
    df1 = spark.read.option("header", True).csv("emp.csv")
    df2 = spark.read.option("header", True).csv("emp.csv")

    # Normalize the DataFrames: sort and drop duplicate rows (if needed)
    df1_sorted = df1.sort(df1.columns).dropDuplicates()
    df2_sorted = df2.sort(df2.columns).dropDuplicates()

    # Compare row count
    assert df1_sorted.count() == df2_sorted.count(), "Row counts do not match."

    # Compare content: subtracting both ways
    diff1 = df1_sorted.subtract(df2_sorted)
    diff2 = df2_sorted.subtract(df1_sorted)

    assert diff1.count() == 0 and diff2.count() == 0, "DataFrames do not match."


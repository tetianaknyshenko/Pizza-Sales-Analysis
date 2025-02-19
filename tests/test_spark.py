from pyspark.sql import SparkSession

def test_spark_session():
    spark = SparkSession.builder.appName("TestSession").getOrCreate()
    assert spark is not None
    print("✅ Spark Session Created Successfully!")

if __name__ == "__main__":
    test_spark_session()
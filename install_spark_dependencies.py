from pyspark.sql import SparkSession

# This will download the Jar packages.
SparkSession.builder.appName("console config").config('spark.jars.packages','org.apache.spark').getOrCreate()

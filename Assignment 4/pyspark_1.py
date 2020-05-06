from pyspark.sql import SQLContext
from pyspark import SparkContext,SparkConf
import pyspark.sql.functions as ssql
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
cpu=int(sys.argv[1])
file_path=sys.argv[2]
spark = SparkSession.builder.appName("groupbyagg").getOrCreate()
dataframe = spark.read.csv('airports.csv', inferSchema=True, header=True)
dataframe=dataframe.repartition(cpu)
data=dataframe.groupBy('COUNTRY').agg(ssql.count('COUNTRY').alias('TOTAL_COUNT'))
data.toPandas().to_csv(file_path)

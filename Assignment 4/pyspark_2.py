from pyspark.sql.functions import *
from pyspark.sql.types import *
import pyspark.sql.functions as ssql
from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import sys
cpu=int(sys.argv[1])
file_path=sys.argv[2]
spark = SparkSession.builder.appName('groupbyagg').getOrCreate()
dataframe = spark.read.csv('airports.csv', inferSchema=True, header=True)
dataframe=dataframe.repartition(cpu)
data=dataframe.groupBy('COUNTRY').agg(ssql.count('COUNTRY').alias('TOTAL_COUNT')).sort(desc('TOTAL_COUNT')).limit(1)
data=data.select('COUNTRY')
data.toPandas().to_csv(file_path)

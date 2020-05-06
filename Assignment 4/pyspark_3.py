from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import sys
from pyspark.sql.functions import *
cpu=int(sys.argv[1])
file_path=sys.argv[2]
spark = SparkSession.builder.appName("groupbyagg").getOrCreate()
dataframe= spark.read.csv('airports.csv', inferSchema=True, header=True)
dataframe=dataframe.repartition(cpu)
data=dataframe.filter(col("LATITUDE").between("10","90")).filter(col("LONGITUDE").between("-90","-10"))
data=data.select('NAME')
data.toPandas().to_csv(file_path)

from pyspark import SparkContext
from pyspark import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


if __name__ == '__main__':
	
	sc = sparkContext.getOrCreate()
	
	sqlContext = SQLContext(sc)
	
	df = spark.read.csv('linkToS3Bucket', inferSchema = True, header = True, )
	cleaningdf = df.dropna(thresh=3)
	
	cleaningdf = cleaningdf.fillna(0)
	
	cleaningdf.registerTempTable('df_table')
	
	sqlContext.sql('select * from df_table').show()
	
	cleaningdf.write.csv('linkToS3Bucket')
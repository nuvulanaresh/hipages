import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *

context = SparkContext('local[*]')
spark = SparkSession(context)
#context.setLogLevel('WARN')
#scope for parameterization
jsonpath="/home/jovyan/work/data/source_event_data.json"
user_activity_df = (spark.read\
    .option("header","false")\
    .option("inferSchema","true")\
    .json(jsonpath)
    .select(col("event_id"),col("user.id").alias("user_id"),col("action").alias("activity"),"url",col("timestamp").alias("time_stamp"))\
    .withColumn("url_level1",concat(split(("url"),'\\.').getItem(1),lit('.'),split(("url"),'\\.').getItem(2)))\
    .withColumn("url_sub_level",split(("url"),'\\.').getItem(3))\
    .withColumn("url_level2",split(("url_sub_level"),"/").getItem(1))\
    .withColumn("url_level3",split(("url_sub_level"),"/").getItem(2))\
    .select("user_id","time_stamp","url_level1","url_level2","url_level3","activity")
    )
#print(user_activity_df.show(5))
#Writing the User Activity DataFrame to csv file
user_activity_df.write\
    .option("header","true")\
    .option("sep",",")\
    .mode("overwrite")\
    .csv("/home/jovyan/work/data/user_activity")

# user_activity_df.write\
#     .format("csv")\
#     .mode("overwrite")\
#     .saveAsTable("hipages_user_activity")

hrly_granular_activtiy_df = (user_activity_df\
    .withColumn("time_bucket", from_unixtime(unix_timestamp(col("time_stamp"), "MM/dd/yyyy HH:mm:ss"), "yyyyMMddHH"))\
    .groupBy("time_bucket","url_level1","url_level2","activity")\
    .agg(count("activity").alias("activity_count"),countDistinct("user_id").alias("user_count"))
    )

hrly_granular_activtiy_df.write\
    .option("header","true")\
    .option("sep",",")\
    .mode("overwrite")\
    .csv("/home/jovyan/work/data/hrly_granular_activtiy")

# hrly_granular_activtiy_df.write\
#     .format("csv")\
#     .mode("overwrite")\
#     .saveAsTable("hipages_hrly_granular_activity")

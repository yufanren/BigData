import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import format_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires 1 input file", file=sys.stderr)
        exit(-1)
    spark = SparkSession.builder.getOrCreate()
    pv = spark.read.options(header='true', inferSchema='true').csv(sys.argv[1])
    pv1 = pv.filter(pv["registration_state"] == 'NY')
    pv2 = pv.filter(pv["registration_state"] != 'NY')
    pv1.createOrReplaceTempView("pv1")
    pv2.createOrReplaceTempView("pv2")

    other = spark.sql('select count(*) from pv2').collect()[0]['count(1)']
    newrow = spark.createDataFrame([('Other', other)])
    result = spark.sql('select registration_state, count(*) counts from pv1 group by registration_state')\
        .union(newrow)
    result.select(format_string('%s\t%d',result.registration_state,result.counts))\
        .write.save("task4-sql.out", format="text")

    spark.stop()


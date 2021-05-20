import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import format_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires 1 input file", file=sys.stderr)
        exit(-1)
    spark = SparkSession.builder.getOrCreate()
    pv = spark.read.options(header='true', inferSchema='true').csv(sys.argv[1])
    pv.createOrReplaceTempView("pv")

    result = spark.sql('select plate_id, registration_state, count(*) counts from pv group by plate_id,'
                       ' registration_state order by counts desc, plate_id, registration_state limit 20')
    result.select(format_string('%s, %s\t%d', result.plate_id, result.registration_state, result.counts))\
      .write.save("task6-sql.out", format="text")

    spark.stop()
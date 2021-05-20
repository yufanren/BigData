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

    result = spark.sql('select violation_code, count(summons_number) count from pv'
                       ' group by violation_code order by violation_code')

    result.select(format_string('%d\t%d', result.violation_code, result['count'])) \
        .write.save("task2-sql.out", format="text")

    spark.stop()

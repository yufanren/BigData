import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import format_string, udf

def twoDecimal(num):
  return str("{:.2f}".format(num))

two_decimal = udf(lambda n: twoDecimal(n))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires 1 input file", file=sys.stderr)
        exit(-1)
    spark = SparkSession.builder.getOrCreate()
    ov = spark.read.options(header='true', inferSchema='true').csv(sys.argv[1])
    ov.createOrReplaceTempView("ov")

    result = spark.sql('select license_type, sum(amount_due) total_due, avg(amount_due)'
                       ' avg_due from ov group by license_type order by license_type')

    result = result.withColumn("total_due_str", two_decimal("total_due"))\
      .withColumn("avg_due_str", two_decimal("avg_due"))

    result.select(format_string('%s\t%s, %s', result.license_type, result.total_due_str,
                                result.avg_due_str)).write.save("task3-sql.out", format="text")

    spark.stop()
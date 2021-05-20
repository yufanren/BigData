import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import format_string, udf

def isWeekday(day):
  return 0 if day in {'05', '06', '12', '13', '19', '20', '26', '27'} else 1

def isWeekend(day):
  return 1 if day in {'05', '06', '12', '13', '19', '20', '26', '27'} else 0

def twoDecimal(num):
  return str("{:.2f}".format(num))

def splitDate(date):
    return date.strip().split('-')[2]

is_weekday = udf(lambda d: isWeekday(d))
is_weekend = udf(lambda d: isWeekend(d))
two_decimal = udf(lambda n: twoDecimal(n))
split_udf = udf(lambda s: splitDate(s))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Requires 1 input file", file=sys.stderr)
    exit(-1)
  spark = SparkSession.builder.getOrCreate()
  pv = spark.read.options(header='true', inferSchema='false').csv(sys.argv[1])

  pv_simplified = pv.select("violation_code", split_udf("issue_date").alias("issue_day")) \
    .withColumn("weekend_ct", is_weekend("issue_day")) \
    .withColumn("weekday_ct", is_weekday("issue_day"))

  pv_simplified.createOrReplaceTempView("pv")
  result = spark.sql('select violation_code, sum(weekend_ct) / 8 weekend_avg_count,'
                     ' sum(weekday_ct) / 23 weekday_avg_count '
                     'from pv group by violation_code order by cast(violation_code as int)')

  result = result.withColumn("weekend_avg", two_decimal("weekend_avg_count")) \
    .withColumn("weekday_avg", two_decimal("weekday_avg_count"))

  result.select(format_string('%s\t%s, %s', result.violation_code, result.weekend_avg,
                              result.weekday_avg)).write.save("task7-sql.out", format="text")
  spark.stop()
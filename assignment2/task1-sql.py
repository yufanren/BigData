import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import format_string, date_format

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Requires 2 input files", file=sys.stderr)
        exit(-1)
    spark = SparkSession.builder.getOrCreate()
    pv = spark.read.options(header='true', inferSchema='true').csv(sys.argv[1])
    ov = spark.read.options(header='true', inferSchema='true').csv(sys.argv[2])
    pv.createOrReplaceTempView("pv")
    ov.createOrReplaceTempView("ov")

    result = spark.sql('select summons_number, plate_id, violation_precinct, violation_code, issue_date'
              ' from pv where summons_number not in (select summons_number from ov) order by summons_number')
    result.select(format_string('%d\t%s, %d, %d, %s',result.summons_number,result.plate_id,result.violation_precinct,
        result.violation_code,date_format(result.issue_date, 'yyyy-MM-dd')))\
        .write.save("task1-sql.out", format="text")

    spark.stop()





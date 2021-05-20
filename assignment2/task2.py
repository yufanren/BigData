import sys
from csv import reader
from pyspark import SparkContext
from operator import add

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires 1 input file", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1).mapPartitions(lambda x: reader(x))
    violation_by_code = lines.map(lambda x: (int(x[2]), 1))\
        .reduceByKey(add)\
        .sortByKey()\
        .map(lambda x: str(x[0]) + '\t' + str(x[1]))

    violation_by_code.saveAsTextFile("task2.out")
    sc.stop()
import sys
from csv import reader
from pyspark import SparkContext
from operator import add


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires 1 input file", file=sys.stderr)
        exit(-1)
    sc = SparkContext()

    lines = sc.textFile(sys.argv[1], 1)\
      .mapPartitions(lambda x: reader(x))
    top = lines.map(lambda x: (x[14] + ', ' + x[16], 1))\
      .reduceByKey(add)\
      .max(lambda x: x[1])

    sc.parallelize([top[0] + '\t' + str(top[1])]).saveAsTextFile("task5.out")
    sc.stop()
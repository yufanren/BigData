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
        .sortByKey()\
        .sortBy(keyfunc=lambda x: x[1], ascending=False)\
        .map(lambda x: x[0] + '\t' + str(x[1]))\
        .take(20)

    sc.parallelize(top).saveAsTextFile("task6.out")
    sc.stop()
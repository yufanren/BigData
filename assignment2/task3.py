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
    counts = lines.map(lambda x: (x[2], 1))\
        .reduceByKey(add)
    total = lines.map(lambda x: (x[2], float(x[12]) if x[12] else 0))\
        .reduceByKey(add)
    results = total.join(counts)\
        .sortByKey()\
        .map(lambda x: x[0] + '\t' + str("{:.2f}".format(x[1][0])) + ', ' + str("{:.2f}".format(x[1][0] / x[1][1])))

    results.saveAsTextFile("task3.out")
    sc.stop()
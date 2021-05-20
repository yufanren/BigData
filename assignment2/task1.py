import sys
from csv import reader
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Requires 2 input files", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines_open = sc.textFile(sys.argv[2], 1)\
      .mapPartitions(lambda x: reader(x))\
      .map(lambda x: x[0])\
      .collect()
    open_list = set(lines_open)

    violations = sc.textFile(sys.argv[1], 1)\
      .mapPartitions(lambda x: reader(x))\
      .filter(lambda x: (x[0] not in open_list))\
      .sortBy(lambda x: x[0])\
      .map(lambda x: x[0] + '\t' + ', '.join([x[14], x[6], x[2], x[1]]))

    violations.saveAsTextFile("task1.out")

    sc.stop()

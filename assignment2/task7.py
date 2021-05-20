import sys
from csv import reader
from pyspark import SparkContext

weekend = {'05', '06', '12', '13', '19', '20', '26', '27'}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires 1 input file", file=sys.stderr)
        exit(-1)
    sc = SparkContext()

    lines = sc.textFile(sys.argv[1], 1).mapPartitions(lambda x: reader(x))

    code_counts = lines.map(lambda x: (int(x[2]), [1, 0]) if (x[1].strip().split('-')[2] in weekend) else (int(x[2]), [0, 1]))\
      .reduceByKey(lambda x, y: [x[0] + y[0], x[1] + y[1]])\
      .sortByKey()\
      .map(lambda x: str(x[0]) + '\t' + str("{:.2f}".format(x[1][0] / 8)) + ', ' + str("{:.2f}".format(x[1][1] / 23)))

    code_counts.saveAsTextFile("task7.out")
    sc.stop()

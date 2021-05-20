import sys
from csv import reader
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Requires 1 input file", file=sys.stderr)
        exit(-1)
    sc = SparkContext()

    lines = sc.textFile(sys.argv[1], 1).mapPartitions(lambda x: reader(x))
    NY_count = lines.filter(lambda x: x[16] == 'NY').count()
    Other_count = lines.count() - NY_count
    result = sc.parallelize(['NY\t' + str(NY_count), 'Other\t' + str(Other_count)])

    result.saveAsTextFile("task4.out")
    sc.stop()
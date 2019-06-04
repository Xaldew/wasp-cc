#!/usr/bin/env python

import sys
import locale
import argparse
import pyspark
import pyspark.sql
import pyspark.mllib.linalg
import pyspark.mllib.linalg.distributed


def main(args):
    """Compute the Singular Value Decomposition (SVD) of a matrix.

    .. Keyword Arguments:
    :param args: The program arguments.

    .. Types:
    :type args: A argparse namespace ojects containing the program arguments.

    .. Returns:
    :returns: 0 If the program ran successfully, otherwise non-zero.
    :rtype: An integer.

    """
    conf = (pyspark.SparkConf()
            .setAppName("SVD")
            .set("spark.hadoop.validateOutputSpecs", "false")
            # .set("spark.executor.instances", 8)
            # .set("spark.executor.cores", 1)
            # .set("spark.dynamicAllocation.enabled", False)
            # .set("spark.executor.memory", "4g")
            # .set("spark.driver.memory", "4g")
            # .set("spark.driver.maxResultSize", "4g")
    )
    sc = pyspark.SparkContext(conf=conf)

    # Required to get access to the `toDF()` function inside of CoordinateMatrix.
    spark = pyspark.sql.SparkSession(sc)

    # Re-create the row-matrix.
    rows = sc.pickleFile(args.rows)
    rm = pyspark.mllib.linalg.distributed.RowMatrix(rows)

    # Compute the SVD, store the singular values in the output.
    k = min(100, rm.numCols())
    svd = rm.computeSVD(k)
    sc.parallelize(svd.s).saveAsTextFile(args.S)

    return 0


def parse_arguments(argv):
    """Parse the given argument vector.

    .. Keyword Arguments:
    :param argv: The arguments to be parsed.

    .. Types:
    :type argv: A list of strings.

    .. Returns:
    :returns: The parsed arguments.
    :rtype: A argparse namespace object.

    """
    fmtr = argparse.RawDescriptionHelpFormatter
    kdesc = "Python Spark SVD script."
    parser = argparse.ArgumentParser(description=kdesc, formatter_class=fmtr)
    parser.add_argument("rows", metavar="RDD", type=str,
                        help="The matrix to read.")
    parser.add_argument("S", metavar="RDD", type=str,
                        help="Output RDD continaing the singular values.")
    return parser.parse_args(argv)


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "")
    ARGS = parse_arguments(sys.argv[1:])
    sys.exit(main(ARGS))

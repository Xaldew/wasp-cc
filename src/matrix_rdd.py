#!/usr/bin/env python
# Create a spark Matrix RDD for future use.

import sys
import locale
import argparse
import numpy
import tempfile
import scipy
import scipy.io
import scipy.sparse.linalg
import pyspark
import pyspark.sql
import pyspark.mllib.linalg
import pyspark.mllib.linalg.distributed


def main(args):
    """Convert the matrix into a RDD.

    .. Keyword Arguments:
    :param args: The program arguments.

    .. Types:
    :type args: A argparse namespace ojects containing the program arguments.

    .. Returns:
    :returns: 0 If the program ran successfully, otherwise non-zero.
    :rtype: An integer.

    """
    conf = pyspark.SparkConf().set("spark.hadoop.validateOutputSpecs", "false")
    sc = pyspark.SparkContext(conf=conf)
    spark = pyspark.sql.SparkSession(sc)

    # Write the file to a temporaryfile so we can actually convert it.
    A = sc.textFile(args.A)
    tmp = tempfile.TemporaryFile()
    tmp.write("\n".join(A.collect()))
    tmp.seek(0)

    # Read the matrix using SciPy and convert to coordinate-matrix.
    a = scipy.io.mmread(tmp)
    s = a.shape
    coo = sc.parallelize(list((r, c, v) for ((r, c), v) in a.todok().items()))

    # Convert the matrix to the PySpark representation and save the RDD.
    mat = pyspark.mllib.linalg.distributed.CoordinateMatrix(coo, s[0], s[1])
    mat.entries.saveAsTextFile(args.O)

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
    kdesc = "Python Spark Matrix construction script."
    parser = argparse.ArgumentParser(description=kdesc, formatter_class=fmtr)
    parser.add_argument("A", metavar="A", type=str,
                        help="The matrix to read.")
    parser.add_argument("O", metavar="OUT", type=str,
                        help="Output name for the Spark RDD.")
    return parser.parse_args(argv)


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "")
    ARGS = parse_arguments(sys.argv[1:])
    sys.exit(main(ARGS))

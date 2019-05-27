#!/usr/bin/env python3
# Perform GEMM on two matrices using SciPy.

import sys
import locale
import scipy
import scipy.io
import numpy
import argparse


def main(args):
    """Perform general matrix multiplication.

    .. Keyword Arguments:
    :param args: The program arguments.

    .. Types:
    :type args: A argparse namespace ojects containing the program arguments.

    .. Returns:
    :returns: 0 If the program ran successfully, otherwise non-zero.
    :rtype: An integer.

    """
    a = scipy.io.mmread(args.A)
    b = scipy.io.mmread(args.B)
    c = a.dot(b)
    if args.facit:
        facit = scipy.io.mmread(args.facit)
        if np.allclose(c, facit):
            return 0
        else:
            return 1
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
    kdesc = "Python GEMM script."
    parser = argparse.ArgumentParser(description=kdesc, formatter_class=fmtr)
    parser.add_argument("A", metavar="A", type=argparse.FileType("r"),
                        help="The first matrix to read.")
    parser.add_argument("B", metavar="B", type=argparse.FileType("r"),
                        help="The second matrix to read.")
    parser.add_argument("-f", "--facit", type=argparse.FileType("r"),
                        help="A file containing the correct results.")
    return parser.parse_args(argv)


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "")
    ARGS = parse_arguments(sys.argv[1:])
    sys.exit(main(ARGS))

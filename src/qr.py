#!/usr/bin/env python3
# Perform QR decomposition of a matrix.

import sys
import locale
import scipy
import scipy.io
import scipy.sparse.linalg
import sparseqr
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
    Q, R, e, rank = sparseqr.qr(a)
    print("Rank: %d." % rank)
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
    kdesc = "Python QR decomposition script."
    parser = argparse.ArgumentParser(description=kdesc, formatter_class=fmtr)
    parser.add_argument("A", metavar="A", type=argparse.FileType("r"),
                        help="The matrix to read.")
    return parser.parse_args(argv)


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "")
    ARGS = parse_arguments(sys.argv[1:])
    sys.exit(main(ARGS))

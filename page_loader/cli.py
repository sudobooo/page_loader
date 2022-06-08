"""Parsing arguments from CLI"""

import argparse  # pragma: no cover
import os  # pragma: no cover


def parse():  # pragma: no cover
    """Parse arguments from CLI.
    Return arguments as a string."""

    parser = argparse.ArgumentParser(
        description='description: web page downloader',
        prog='page-loader',
        usage='%(prog)s [options] <url>'
    )

    parser.add_argument(
        '-V', '--version',
        version='%(prog)s 1.0',
        action='version',
        help='output the version number'
    )

    parser.add_argument(
        '-o', '--output',
        help='output dir (default: working directory)',
        metavar='[dir]',
        default=os.getcwd()
    )

    parser.add_argument(
        'url',
        type=str
    )

    args = parser.parse_args()

    return args

#!/usr/bin/env python3

"""page_loader script."""
import os  # pragma: no cover
import sys  # pragma: no cover
import argparse  # pragma: no cover
import logging.config  # pragma: no cover

from page_loader import download  # pragma: no cover
from page_loader.logging_settings import LOGGING_CONFIG  # pragma: no cover

SUCCES = 'Content was downloaded while pathing to '


def main():  # pragma: no cover

    logging.config.dictConfig(LOGGING_CONFIG)

    parser = argparse.ArgumentParser(
        description='description: web page downloader',
        prog='page-loader',
        usage='%(prog)s [options] <url>',
        add_help=False
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
        '-h', '--help', action='help',
        default=argparse.SUPPRESS,
        help='display help for command'
    )

    parser.add_argument(
        'url',
        type=str
    )

    parser._optionals.title = 'options'

    args = parser.parse_args()

    try:
        print(f'{SUCCES}{download(args.url, args.output)}')
    except Exception:
        sys.exit(1)


if __name__ == '__main__':  # pragma: no cover
    main()

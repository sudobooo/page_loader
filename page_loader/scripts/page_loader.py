#!/usr/bin/env python3

"""page_loader script."""
import os
import argparse
import logging.config

from page_loader import download
from page_loader.logging_settings import LOGGING_CONFIG


def main():

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

    print(download(args.url, args.output))


if __name__ == '__main__':
    main()

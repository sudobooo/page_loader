#!/usr/bin/env python3

"""page_loader script."""
import os
import sys
import argparse
import logging.config

from page_loader import download
from page_loader.logging_settings import LOGGING_CONFIG
from page_loader.logging_settings import log_error, log_info

CHECK_PERMISSION = 'Check directory permissions: '
CHECK_FILE = 'File or directory does not exist: '
CHECK_OPTION = 'Please write "-h" to see the available options'


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

    try:
        print(download(args.url, args.output))
    except PermissionError as permission:
        log_error.error(permission)
        log_info.info(f'{CHECK_PERMISSION}{permission.filename}')
        sys.exit(1)
    except FileNotFoundError as file_not_found:
        log_error.error(file_not_found)
        log_info.info(f'{CHECK_FILE}{file_not_found.filename}')
        sys.exit(1)
    except KeyError as key_error:
        log_error.error(key_error)
        log_info.info(CHECK_OPTION)
        sys.exit(1)


if __name__ == '__main__':
    main()

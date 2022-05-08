import argparse
import os


def parse_cli_args():
    parser = argparse.ArgumentParser(
                            description='description: web page downloader',
                            prog='page-loader',
                            usage='%(prog)s [options] <url>',
                            add_help=False
                            )

    parser.add_argument('-V', '--version',
                        version='%(prog)s 1.0',
                        action='version',
                        help='output the version number'
                        )

    parser.add_argument('-o', '--output',
                        help='output dir (default: working directory)',
                        metavar='[dir]',
                        default=os.getcwd()
                        )

    parser.add_argument('-h', '--help', action='help',
                        default=argparse.SUPPRESS,
                        help='display help for command'
                        )

    parser.add_argument('url', type=str)

    parser._optionals.title = 'options'

    args = parser.parse_args()

    return args

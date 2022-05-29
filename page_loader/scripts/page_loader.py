#!/usr/bin/env python3

"""page_loader script."""
import sys  # pragma: no cover
import logging.config  # pragma: no cover

from page_loader import download
from page_loader.logging_settings import LOGGING_CONFIG
from page_loader.cli_parser import cli_parse

SUCCES = 'Content was downloaded while pathing to '


def main():

    logging.config.dictConfig(LOGGING_CONFIG)  # pragma: no cover

    args = cli_parse()

    try:
        print(f'{SUCCES}{download(args.url, args.output)}')
    except Exception:
        sys.exit(1)


if __name__ == '__main__':  # pragma: no cover
    main()

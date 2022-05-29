#!/usr/bin/env python3

"""page_loader script."""
import sys  # pragma: no cover

from page_loader import download
from page_loader.cli_parser import cli_parse


def main():

    args = cli_parse()

    try:
        download(args.url, args.output)
    except Exception:
        sys.exit(1)


if __name__ == '__main__':  # pragma: no cover
    main()

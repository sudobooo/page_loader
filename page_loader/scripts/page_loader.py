#!/usr/bin/env python3

"""page_loader script."""

import sys  # pragma: no cover

from page_loader import download
from page_loader import cli


def main():
    """Parse values from CLI.
    Starts the download.
    Checks for exceptions that should terminate the program."""

    args = cli.parse()

    try:
        download(args.url, args.output)
    except Exception:
        sys.exit(1)


if __name__ == '__main__':  # pragma: no cover
    main()

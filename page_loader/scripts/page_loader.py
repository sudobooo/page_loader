#!/usr/bin/env python3

"""page_loader script."""
from page_loader.cli import parse_cli_args
from page_loader import download


def main():

    args = parse_cli_args()

    print(download(args.url, args.output))


if __name__ == '__main__':
    main()

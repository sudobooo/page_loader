"""Converts the url to the required name for naming a file or directory."""

import re
from urllib.parse import urlparse


def convert_name(url):
    """Takes one argument:
    'url' is text link to website.
    Returns convert name for the file and its format,
    if the format exists."""

    parse_link = urlparse(url)
    without_scheme = parse_link.netloc
    format = f"{parse_link.path.split('.')[-1]}".rstrip('/')
    path = parse_link.path[:-len(format) - 1].rstrip('/')

    if len(path) != 0:
        result = replace_chars(f'{without_scheme}{path}')
    else:
        result = replace_chars(f'{without_scheme}{format}')
        format = ''

    return result, format


def convert(url, type=None):
    """Takes two arguments:
    'url' is text link to website,
    'type' is specifies whether the name is for a file or for a directory.
    Returns the finished name."""

    result, format = convert_name(url)
    type_dict = {'dir': '_files'}

    if type is not None:
        extension = type_dict.get(type)
        return f'{result}{extension}'

    output = f'{result}.{format}'
    if output.endswith('.'):
        output += 'html'
    return output


def replace_chars(text):
    """Takes one argument:
    'text' is text string.
    Returns text where non-numeric and non-alphabetic
    characters are replaced by '-'"""

    result = re.sub(r"[^0-9a-zA-Z]", "-", f'{text}')

    return result

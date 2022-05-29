import re
from urllib.parse import urlparse


def convert_name(url):

    parse_link = urlparse(url)
    without_scheme = parse_link.netloc
    format = f"{parse_link.path.split('.')[-1]}".rstrip('/')

    if len(format) >= 0:
        path = parse_link.path[:-len(format) - 1].rstrip('/')

    if len(path) != 0:
        result = replace_chars(f'{without_scheme}{path}')
    else:
        result = replace_chars(f'{without_scheme}{format}')
        format = ''

    return result, format


def convert(text, type=None):

    result, format = convert_name(text)
    type_dict = {'html': '.html',
                 'dir': '_files'
                 }

    if type is not None:
        extension = type_dict.get(type)
        return f'{result}{extension}'

    output = f'{result}.{format}'
    if output.endswith('.'):
        output += 'html'
    return output


def replace_chars(text):

    result = re.sub(r"[^0-9a-zA-Z]", "-", f'{text}')

    return result

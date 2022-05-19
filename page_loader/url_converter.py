import re
import os
from urllib.parse import urlparse


def convert(url, type='html'):
    parse_link = urlparse(url)
    path = ''.join([parse_link.netloc, parse_link.path])
    file_name, extension = os.path.splitext(path)
    result = re.sub(r"\W", "-", file_name)

    type_dict = {'html': '.html',
                 'dir': '_files',
                 'png': '.png'
                 }
    type_file = type_dict.get(type)

    if extension == type_file:
        return f'{result}{extension}'
    else:
        return f'{result}{extension}{type_file}'

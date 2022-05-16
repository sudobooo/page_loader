import re


def convert_name(text):
    without_scheme = re.search(r"//+(.*)", text).group(1)
    result = re.sub(r"[^0-9a-zA-Z]", "-", without_scheme)

    result = result.rstrip('-html')
    return result


def convert(text, type='html'):
    result = convert_name(text)
    type_dict = {'html': '.html',
                 'dir': '_files',
                 'png': '.png'
                 }
    extension = type_dict.get(type)

    try:
        result += extension
        return result
    except TypeError:
        return 'This file or directory extension is not supported!'

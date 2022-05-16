import re


def convert_name(text):
    without_scheme = re.search(r"//+(.*)", text).group(1)
    result = re.sub(r"[^0-9a-zA-Z]", "-", without_scheme)

    result = result.rstrip('-html')
    return result


def convert(text, type='html'):
    result = convert_name(text)

    if type == 'html':
        result += '.html'
    elif type == 'dir':
        result += '_files'
    return result

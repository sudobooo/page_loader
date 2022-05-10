import re


def convert(text):
    without_scheme = re.search(r"//+(.*)", text).group(1)
    result = re.sub(r"[^0-9a-zA-Z]", "-", without_scheme)

    if result.endswith('html'):
        result = result.rstrip('-html')
        result += '.html'
    else:
        result += '.html'
    return result

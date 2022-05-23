from urllib.parse import urljoin, urlparse


def same_netloc(first_url, second_url):

    first_parse_link = urlparse(first_url)
    second_parse_link = urlparse(second_url)

    return first_parse_link.netloc == second_parse_link.netloc


def check_content(url, content):

    if content.startswith('http'):
        if not same_netloc(content, url):
            return False
        return content
    if not content.startswith('/'):
        content = '/' + content
    content_link = urljoin(url, content)
    return content_link

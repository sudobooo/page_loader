"""Checking url addresses with content"""

from page_loader.logging_settings import log_error
from urllib.parse import urljoin, urlparse

NOT_FOUND_FILE = "Attributes src weren't found in {0}\n"
NOT_SAME = "Content was not downloaded because it's on a different host:"


def same_netloc(first_url, second_url):
    """Takes two arguments: 'first_url' and 'second_url'.
    Checks if the netlock is the same.
    Return True of False."""

    first_parse_link = urlparse(first_url)
    second_parse_link = urlparse(second_url)

    return first_parse_link.netloc == second_parse_link.netloc


def check_content(url, content, teg):
    """Takes three arguments:
    'url' is website address,
    'content' is url with content,
    'teg' is HTML tag containing url with content.
    Return valid url link with content."""

    try:
        if content.startswith('http'):
            if not same_netloc(content, url):
                log_error.error(f'{NOT_SAME} {content}')
                return False
            return content

        if not content.startswith('/'):
            content = '/' + content
        content_link = urljoin(url, content)
        return content_link
    except AttributeError:
        log_error.error(NOT_FOUND_FILE.format(teg))

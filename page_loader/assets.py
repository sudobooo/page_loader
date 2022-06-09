"""Collecting a list of resources with content for download"""

import os

from page_loader.logging_settings import log_error
from urllib.parse import urljoin, urlparse
from page_loader import url


def get_resources(data, link, dir):
    """Takes three arguments:
    'data' is html page data,
    'link' is link to download page,
    'dir' is path to the directory to save a content.
    Returns a list of resources to download.
    """

    TAGS_AND_ATTRIBUTES = {
        'img': 'src',
        'script': 'src',
        'link': 'href',
    }
    resources = []

    for teg in data.find_all(TAGS_AND_ATTRIBUTES.keys()):

        attribute = TAGS_AND_ATTRIBUTES.get(teg.name)
        content = teg.get(attribute)
        content_link = check_content(link, content, teg)
        if not content_link:
            continue
        resources.append(content_link)

        teg[attribute] = os.path.join(dir, url.to_filename(content_link))
    return resources


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
                log_error.error(f"Content was not downloaded because it's"
                                f' on a different host: {content}')
                return False
            return content

        if not content.startswith('/'):
            content = '/' + content
        content_link = urljoin(url, content)
        return content_link
    except AttributeError:
        log_error.error("Attributes src weren't found in {0}\n".format(teg))

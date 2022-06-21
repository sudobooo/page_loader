"""Collecting a list of resources with content for download"""

import os
import requests
from bs4 import BeautifulSoup

from page_loader.logging_settings import log_error, ExpectedException
from urllib.parse import urljoin, urlparse
from page_loader import url


def get_resources(response, link, dir):
    """Takes three arguments:
    'response' is html page,
    'link' is link to download page,
    'dir' is path to the directory to save a content.
    Returns a list of resources to download.
    """

    TAGS_AND_ATTRIBUTES = {
        'img': 'src',
        'script': 'src',
        'link': 'href',
    }
    data = BeautifulSoup(response.text, 'html.parser')
    resources = []

    for teg in data.find_all(TAGS_AND_ATTRIBUTES.keys()):

        attribute = TAGS_AND_ATTRIBUTES.get(teg.name)
        content = teg.get(attribute)
        if content is None:
            log_error.error(f"Attributes src weren't found in {teg}\n")
            continue
        if content.startswith('http'):
            if not urlparse(link).netloc == urlparse(content).netloc:
                log_error.error(f"Content was not downloaded because it's"
                                f' on a different host: {content}')
                continue
            content_link = content
        else:
            if not content.startswith('/'):
                content = '/' + content
            content_link = urljoin(link, content)
        resources.append(content_link)

        teg[attribute] = os.path.join(dir, url.to_filename(content_link))
    return resources, data.prettify()


def get_data(link):
    """'link' is url to web page.
    Returns response."""

    try:
        response = requests.get(link)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ExpectedException(error)
    return response

"""Downloading content from a web page"""

import os
import requests
from progress.bar import ShadyBar

from page_loader import url
from page_loader.resources import check_content
from page_loader.writer import write_content
from page_loader.logging_settings import log_error


def download_content(data, link, dir, path):  # noqa: C901
    """Takes four arguments:
    'data' is html page data,
    'link' is link to download page,
    'dir' is path to the directory to save a content,
    'path' is full path to content.
    The result of execution is the write content."""

    TAGS_AND_ATTRIBUTES = {
        'img': 'src',
        'script': 'src',
        'link': 'href',
    }

    len_for_bar = len(data.find_all(TAGS_AND_ATTRIBUTES.keys()))
    with ShadyBar('Downloading',
                  max=len_for_bar,
                  suffix='%(percent)d%%') as bar:

        for teg in data.find_all(TAGS_AND_ATTRIBUTES.keys()):

            bar.next()

            attribute = TAGS_AND_ATTRIBUTES.get(teg.name)
            content = teg.get(attribute)
            content_link = check_content(link, content, teg)
            if not content_link:
                continue

            path_content = os.path.join(path, url.to_filename(content_link))
            teg[attribute] = os.path.join(dir, url.to_filename(content_link))

            try:
                content_response = requests.get(content_link)
            except requests.exceptions.HTTPError as http_error:
                log_error.error(http_error)
            except requests.exceptions.Timeout as timeout:
                log_error.error(timeout)
            except requests.exceptions.ConnectionError as connection_error:
                log_error.error(connection_error)

            write_content(path_content, content_response.content)

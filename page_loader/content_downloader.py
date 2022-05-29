import os
import requests
from progress.bar import ShadyBar

from page_loader.url_converter import convert
from page_loader.content_checker import check_content
from page_loader.writer import write_content
from page_loader.logging_settings import log_error


def download_content(data, url, dir, path):  # noqa: C901

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
            content_link = check_content(url, content, teg)
            if not content_link:
                continue

            path_content = os.path.join(path, convert(content_link))
            teg[attribute] = os.path.join(dir, convert(content_link))

            try:
                content_response = requests.get(content_link)
                content_response.raise_for_status()
            except requests.exceptions.HTTPError as http_error:
                log_error.error(http_error)
            except requests.exceptions.Timeout as timeout:
                log_error.error(timeout)
            except requests.exceptions.ConnectionError as connection_error:
                log_error.error(connection_error)

            write_content(path_content, content_response.content)

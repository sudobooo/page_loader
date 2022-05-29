import os
import requests

from page_loader.url_converter import convert
from page_loader.content_checker import check_content
from page_loader.writer import write_content
from page_loader.logging_settings import log_info, log_error


def download_content(data, url, dir, path):  # noqa: C901

    TAGS_AND_ATTRIBUTES = {
        'img': 'src',
        'script': 'src',
        'link': 'href',
    }

    for teg in data.find_all(TAGS_AND_ATTRIBUTES.keys()):
        attribute = TAGS_AND_ATTRIBUTES.get(teg.name)
        content = teg.get(attribute)
        content_link = check_content(url, content, teg)
        if not content_link:
            continue

        path_content = os.path.join(path, convert(content_link))
        teg[attribute] = os.path.join(dir, convert(content_link))
        try:
            content_response = requests.get(content_link).content
        except requests.exceptions.HTTPError as http_error:
            log_error.error(http_error)
            log_info.info(f'No access to content: {content_link}')
        except requests.exceptions.Timeout as timeout:
            log_error.error(timeout)
            log_info.info(f'No access to content: {content_link}')
        except requests.exceptions.ConnectionError as connection_error:
            log_error.error(connection_error)
            log_info.info(f'No access to content: {content_link}')
        write_content(path_content, content_response)

import os
import requests

from page_loader.url_converter import convert
from page_loader.content_checker import check_content
from page_loader.writer import write_content
from page_loader.logging_settings import log_info


def download_content(data, url, dir, path):

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

        image_response = requests.get(content_link).content
        write_content(path_content, image_response)
        SUCCES = f'Content was downloaded while pathing to {path_content}'
        log_info.info(SUCCES)

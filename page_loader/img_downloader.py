import os
import requests

from urllib.parse import urljoin, urlparse
from page_loader.url_converter import convert


def download_img(data, url, dir, path):

    block = data.find_all('img')

    for teg in block:
        image = teg.get('src')
        if image.startswith('http'):
            if not same_netloc(image, url):
                continue
            image_link = image
        else:
            if not image.startswith('/'):
                image = '/' + image
            image_link = urljoin(url, image)

        path_image = os.path.join(path,
                                  convert(image_link))
        teg['src'] = os.path.join(dir,
                                  convert(image_link))

        image_response = requests.get(image_link).content
        write_img(path_image, image_response)


def write_html(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def write_img(path, content):
    with open(path, "wb") as file:
        file.write(content)


def same_netloc(first_url, second_url):

    first_parse_link = urlparse(first_url)
    second_parse_link = urlparse(second_url)

    return first_parse_link.netloc == second_parse_link.netloc

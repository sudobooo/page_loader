import os
import requests

from urllib.parse import urljoin
from page_loader.url_converter import convert


def download_img(data, url, dir):

    block = data.find_all('img')

    for teg in block:
        image = teg.get('src')
        if image.startswith('http'):
            image_link = image
        else:
            if not image.startswith('/'):
                image = '/' + image
            image_link = urljoin(url, image)

        image_response = requests.get(image_link).content
        actual_path_image = os.path.join(dir, convert(image_link, 'png'))
        teg['src'] = actual_path_image
        write_img(actual_path_image, image_response)


def write_html(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def write_img(path, content):
    with open(path, "wb") as file:
        file.write(content)

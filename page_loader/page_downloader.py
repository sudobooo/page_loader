import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from page_loader.url_converter import convert


def download(url, path_to_dir=os.getcwd()):
    response = requests.get(url).text
    actual_path_html = os.path.join(path_to_dir, convert(url))
    write_html_to_file(actual_path_html, response)

    soup = BeautifulSoup(response, 'html.parser')
    block = soup.find_all('img')

    for tegs in block:
        image = tegs.get('src')
        if not image.startswith('/'):
            image = '/' + image
        image_link = urljoin(url, image)
        image_response = requests.get(image_link).content
        actual_path_image = os.path.join(path_to_dir, convert(image_link,
                                                              'png'))
        write_img_to_file(actual_path_image, image_response)

    return actual_path_html


def write_html_to_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def write_img_to_file(path, content):
    with open(path, "wb") as file:
        file.write(content)

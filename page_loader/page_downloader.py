import requests
import os
from bs4 import BeautifulSoup

from page_loader.url_converter import convert
from page_loader.img_downloader import download_img, write_html


def download(url, path_to_dir=os.getcwd()):
    response = requests.get(url).text
    dir = convert(url, 'dir')
    actual_path = os.path.join(path_to_dir, dir)
    actual_path_html = os.path.join(path_to_dir, convert(url))

    if not os.path.exists(actual_path):
        os.mkdir(actual_path)

    soup = BeautifulSoup(response, 'html.parser')
    download_img(soup, url, dir, actual_path)

    write_html(actual_path_html, soup.prettify())

    return actual_path

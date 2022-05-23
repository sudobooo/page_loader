import requests
import os
from bs4 import BeautifulSoup

from page_loader.url_converter import convert
from page_loader.img_downloader import download_img
from page_loader.writer import write_html


def download(url, actual_path=os.getcwd()):

    response = requests.get(url).text
    dir = convert(url, 'dir')
    path_to_dir = os.path.join(actual_path, dir)
    path_html = os.path.join(actual_path, convert(url, 'html'))

    if not os.path.exists(path_to_dir):
        os.mkdir(path_to_dir)

    soup = BeautifulSoup(response, 'html.parser')
    download_img(soup, url, dir, path_to_dir)

    write_html(path_html, soup.prettify())

    return path_to_dir

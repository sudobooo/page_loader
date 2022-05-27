import requests
import os
from page_loader.logging_settings import log_error, log_info
from bs4 import BeautifulSoup

from page_loader.url_converter import convert
from page_loader.content_downloader import download_content
from page_loader.writer import write_html, create_dir


def download(url, actual_path=os.getcwd()):

    dir = convert(url, 'dir')
    path_to_dir = os.path.join(actual_path, dir)
    path_html = os.path.join(actual_path, convert(url, 'html'))

    try:
        response = requests.get(url).text
        log_info.info('Successful connection!')
        create_dir(path_to_dir)

        soup = BeautifulSoup(response, 'html.parser')
        download_content(soup, url, dir, path_to_dir)
    except requests.exceptions.Timeout as timeout:
        log_error.error(timeout)
    except requests.exceptions.HTTPError as http_error:
        log_error.error(http_error)
    except requests.exceptions.ConnectionError as connection_error:
        log_error.error(connection_error)

    write_html(path_html, soup.prettify())

    return path_to_dir

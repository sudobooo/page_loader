"""Downloading a web page and saving to the desired path"""

import requests
import os
import logging.config
from page_loader.logging_settings import log_error, log_info
from bs4 import BeautifulSoup

from page_loader import url
from page_loader.content_downloader import download_content
from page_loader.writer import write_html, create_dir
from page_loader.logging_settings import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)  # pragma: no cover


def download(link, actual_path=os.getcwd()):
    """Takes two arguments:
    'link' is link to web page,
    'actual_path' is the path where you want to save the result.
    Returns the path to the downloaded page in html format."""

    check_log = '\nCheck .page-loader-errors.log for details'
    check_url = 'Failed to access the site. Check your internet access or url:'

    dir = url.to_dirname(link)
    path_to_dir = os.path.join(actual_path, dir)
    path_html = os.path.join(actual_path, url.to_filename(link))

    try:
        response = requests.get(link)
        response.raise_for_status()
        log_info.info('Successful connection!')

        create_dir(path_to_dir)

        soup = BeautifulSoup(response.text, 'html.parser')

        download_content(soup, link, dir, path_to_dir)
        log_info.info(f'Content was downloaded while pathing to {path_to_dir}')

        write_html(path_html, soup.prettify())
        log_info.info(f'HTML file was downloaded while pathing to {path_html}')

        return path_html
    except requests.exceptions.Timeout as timeout:
        log_error.error(timeout)
        log_info.info(f'{check_url} {link}{check_log}')
        raise timeout
    except requests.exceptions.HTTPError as http_error:
        log_error.error(http_error)
        log_info.info(f'{check_url} {link}{check_log}')
        raise http_error
    except requests.exceptions.ConnectionError as connection_error:
        log_error.error(connection_error)
        log_info.info(f'{check_url} {link}{check_log}')
        raise connection_error

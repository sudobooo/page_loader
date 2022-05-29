import requests
import os
import logging.config
from page_loader.logging_settings import log_error, log_info
from bs4 import BeautifulSoup

from page_loader.url_converter import convert
from page_loader.content_downloader import download_content
from page_loader.writer import write_html, create_dir
from page_loader.logging_settings import LOGGING_CONFIG

CHECK_URL = 'Failed to access the site. Check your internet access or the url:'
CHECK_LOG = '\nCheck .page-loader-errors.log for details'
SUCCESS = 'Successful connection!'
HTML_DOWNLOAD = 'HTML file was downloaded while pathing to'
CONTENT_DOWNLOAD = 'Content was downloaded while pathing to'


logging.config.dictConfig(LOGGING_CONFIG)  # pragma: no cover


def download(url, actual_path=os.getcwd()):  # noqa: C901

    dir = convert(url, 'dir')
    path_to_dir = os.path.join(actual_path, dir)
    path_html = os.path.join(actual_path, convert(url, 'html'))

    try:
        response = requests.get(url).text
        log_info.info(SUCCESS)

        create_dir(path_to_dir)

        soup = BeautifulSoup(response, 'html.parser')
        download_content(soup, url, dir, path_to_dir)

        write_html(path_html, soup.prettify())
        log_info.info(f'{CONTENT_DOWNLOAD} {path_to_dir}')

        log_info.info(f'{HTML_DOWNLOAD} {path_html}')
        return path_html
    except requests.exceptions.Timeout as timeout:
        log_error.error(timeout)
        log_info.info(f'{CHECK_URL} {url}. {CHECK_LOG}')
        raise timeout
    except requests.exceptions.HTTPError as http_error:
        log_error.error(http_error)
        log_info.info(f'{CHECK_URL} {url}. {CHECK_LOG}')
        raise http_error
    except requests.exceptions.ConnectionError as connection_error:
        log_error.error(connection_error)
        log_info.info(f'{CHECK_URL} {url}. {CHECK_LOG}')
        raise connection_error
    except requests.exceptions.ConnectTimeout as connection_timeout:
        log_error.error(connection_timeout)
        log_info.info(f'{CHECK_URL} {url}. {CHECK_LOG}')
        raise connection_timeout
    except requests.exceptions.TooManyRedirects as too_many_redirects:
        log_error.error(too_many_redirects)
        log_info.info(f'{CHECK_URL} {url}. {CHECK_LOG}')
        raise too_many_redirects

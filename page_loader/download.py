"""Downloading a web page and saving to the desired path"""

import requests
import os
import logging.config
from progress.bar import ShadyBar
from bs4 import BeautifulSoup

from page_loader import url
from page_loader.assets import get_resources
from page_loader.storage import save, create_dir
from page_loader.logging_settings import LOGGING_CONFIG
from page_loader.logging_settings import log_error, log_info


logging.config.dictConfig(LOGGING_CONFIG)  # pragma: no cover


def download(link, actual_path=os.getcwd()):
    """Takes two arguments:
    'link' is url to web page,
    'actual_path' is the path where you want to save the result.
    Returns the path to the downloaded page in html format."""

    response = download_html(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    dir = url.to_dirname(link)
    resources = get_resources(soup, link, dir)

    path_html = os.path.join(actual_path, url.to_filename(link))
    save(path_html, soup.prettify())

    if len(resources) > 0:
        path_to_dir = os.path.join(actual_path, dir)
        create_dir(path_to_dir)
        download_content(resources, path_to_dir)
        log_info.info(f'Content was downloaded while pathing to '
                      f'{path_to_dir}')

    log_info.info(f'HTML file was downloaded while pathing to {path_html}')

    return path_html


def download_html(link):
    """Takes one argument:
    'link' is url to web page.
    Returns response."""

    check_log = '\nCheck .page-loader-errors.log for details'
    check_url = 'Failed to access the site. Check your internet access or url:'

    try:
        response = requests.get(link)
        response.raise_for_status()
        log_info.info('Successful connection!')
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
    return response


def download_content(resources, path):
    """Takes two arguments:
    'resources' is list of download links,
    'path' is full path to content.
    The result of execution is the write content."""

    len_for_bar = len(resources)
    with ShadyBar('Downloading',
                  max=len_for_bar,
                  suffix='%(percent)d%%') as bar:

        for resource in resources:
            bar.next()
            path_content = os.path.join(path, url.to_filename(resource))

            try:
                content_response = requests.get(resource)
            except requests.exceptions.HTTPError as http_error:
                log_error.error(http_error)
            except requests.exceptions.Timeout as timeout:
                log_error.error(timeout)
            except requests.exceptions.ConnectionError as connection_error:
                log_error.error(connection_error)

            save(path_content, content_response.content)

"""Downloading a web page and saving to the desired path"""

import os
import logging.config
import requests
from progress.bar import ShadyBar

from page_loader import url
from page_loader.assets import get_resources, get_data
from page_loader.storage import save, create_dir
from page_loader.logging_settings import LOGGING_CONFIG
from page_loader.logging_settings import log_info, log_error


logging.config.dictConfig(LOGGING_CONFIG)  # pragma: no cover


def download(link, actual_path=os.getcwd()):
    """Takes two arguments:
    'link' is url to web page,
    'actual_path' is the path where you want to save the result.
    Returns the path to the downloaded page in html format."""

    check_log = 'Check .page-loader-errors.log for details'
    check_url = 'Failed to access the site. Check your internet access or url:'

    try:
        response = get_data(link)
        log_info.info('Successful connection!')
    except requests.RequestException as error:
        log_error.error(error)
        log_info.info(f'\n{check_url} {link}\n{check_log}')
        raise error

    dir = url.to_dirname(link)
    resources, changed_html = get_resources(response, link, dir)

    path_html = os.path.join(actual_path, url.to_filename(link))
    save(path_html, changed_html)

    if len(resources) > 0:
        path_to_dir = os.path.join(actual_path, dir)
        create_dir(path_to_dir)
        download_content(resources, path_to_dir)
        log_info.info(f'Content was downloaded while pathing to '
                      f'{path_to_dir}')

    log_info.info(f'HTML file was downloaded while pathing to {path_html}')

    return path_html


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
            try:
                content_response = get_data(resource)
            except requests.RequestException as error:
                log_error.error(error)
            path_content = os.path.join(path, url.to_filename(resource))

            save(path_content, content_response.content)

"""Writes files and creates directories."""

import os
from page_loader.logging_settings import log_info, log_error


def write_html(path, html):
    """Takes two arguments:
    'path' is the path to the file.
    'html' is HTML data.
    The result of the execution is the written
    HTML data at the specified path."""

    with open(path, "w", encoding="utf-8") as file:
        file.write(html)


def write_content(path, content):
    """Takes two arguments:
    'path' is the path to the file.
    'content' is content data.
    The result of the execution is the written
    content data at the specified path."""

    with open(path, "wb") as file:
        file.write(content)


def create_dir(path_to_dir):
    """Takes one argument:
    'path_to_dir' is path to directory.
    The result of the execution is the creation of a directory
    at the specified path or an indication
    that the directory already exists."""

    try:
        if not os.path.exists(path_to_dir):
            os.mkdir(path_to_dir)
            log_info.info(f'Directory was created while pathing to '
                          f'{path_to_dir}')
        else:
            log_info.info('Directory {0} is pre-created'.format(path_to_dir))
    except PermissionError as permission:
        log_error.error(permission)
        log_info.info(f'Check directory permissions: {permission.filename}')
        raise permission
    except FileNotFoundError as file_not_found:
        log_error.error(file_not_found)
        log_info.info(f'File or directory does not exist: '
                      f'{file_not_found.filename}')
        raise file_not_found

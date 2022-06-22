"""Writes files and creates directories."""

import os
from page_loader.logging_settings import log_info, log_error


def save(path, data):
    """Takes two arguments:
    'path' is the path to the file.
    'data' is the data to be written.
    The result of the execution is the written
    data at the specified path."""

    from page_loader import ExpectedException

    try:
        write_mode = 'wb' if isinstance(data, bytes) else 'w'
        with open(path, write_mode) as file:
            file.write(data)
    except OSError as error:
        log_error.error(error)
        log_info.info(str(error))
        raise ExpectedException(error)


def create_dir(path_to_dir):
    """Takes one argument:
    'path_to_dir' is path to directory.
    The result of the execution is the creation of a directory
    at the specified path or an indication
    that the directory already exists."""

    if not os.path.exists(path_to_dir):
        os.mkdir(path_to_dir)
        log_info.info(f'Directory was created while pathing to '
                      f'{path_to_dir}')
    else:
        log_info.info('Directory {0} is pre-created'.format(path_to_dir))

import os
from page_loader.logging_settings import log_info, log_error

CHECK_PERMISSION = 'Check directory permissions: '
CHECK_FILE = 'File or directory does not exist: '


def write_html(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def write_content(path, content):
    with open(path, "wb") as file:
        file.write(content)


def create_dir(path_to_dir):

    CREATED = f'Directory was created while pathing to {path_to_dir}'
    PRE_CREATED = f'Directory {path_to_dir} is pre-created'
    try:
        if not os.path.exists(path_to_dir):
            os.mkdir(path_to_dir)
            log_info.info(CREATED)
        else:
            log_info.info(PRE_CREATED)
    except PermissionError as permission:
        log_error.error(permission)
        log_info.info(f'{CHECK_PERMISSION}{permission.filename}')
        raise permission
    except FileNotFoundError as file_not_found:
        log_error.error(file_not_found)
        log_info.info(f'{CHECK_FILE}{file_not_found.filename}')
        raise file_not_found

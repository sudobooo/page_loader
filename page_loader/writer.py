import os
from page_loader.logging_settings import log_info


def write_html(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def write_content(path, content):
    with open(path, "wb") as file:
        file.write(content)


def create_dir(path_to_dir):

    CREATED = f'Directory was created while pathing to {path_to_dir}.'
    PRE_CREATED = f'Directory {path_to_dir} is pre-created.'

    if not os.path.exists(path_to_dir):
        os.mkdir(path_to_dir)
        log_info.info(CREATED)
    else:
        log_info.info(PRE_CREATED)

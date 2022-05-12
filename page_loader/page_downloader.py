import requests
import os

from page_loader.url_converter import convert


def download(url, path_to_dir=os.getcwd()):
    link = url
    response = requests.get(link).text
    actual_path = os.path.join(path_to_dir, convert(url))
    write_to_file(actual_path, response)

    return actual_path


def write_to_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

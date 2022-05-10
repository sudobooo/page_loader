import requests
import os


def download(path_to_dir, url):
    link = url
    response = requests.get(link).text
    write_to_file(actual_path, response)


def write_to_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

import os
import requests_mock
from tempfile import TemporaryDirectory

from page_loader.page_downloader import download
from page_loader.url_converter import convert


URL = 'https://ru.hexlet.io/courses'
URL_IMAGE = 'https://ru.hexlet.io/assets/professions/python.png'
EXPECTED_NAME = 'ru-hexlet-io-courses.html'
EXPECTED_DIR = 'ru-hexlet-io-courses_files'
EXPECTED_IMG = 'ru-hexlet-io-assets-professions-python.png'


def get_path(name, path='fixtures'):
    return os.path.join('tests', path, name)


def get_content(file):
    with open(file, 'rb') as file:
        return file.read()


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


raw = read(get_path('raw.html'))
expected_html = read(get_path(EXPECTED_NAME))
directory = get_path(EXPECTED_DIR)
image = get_content(os.path.join(directory, EXPECTED_IMG))


def test_convert_url():

    actual = convert(URL)
    assert actual == EXPECTED_NAME


def test_dowloads():

    with requests_mock.Mocker() as m, TemporaryDirectory() as tmpdir:
        m.get(URL, text=raw)
        m.get(URL_IMAGE, content=image)

        expected_path = get_path(EXPECTED_NAME, path=tmpdir)
        actual_path = download(URL, tmpdir)
        assert actual_path == expected_path

        actual_file = read(actual_path)
        assert actual_file == expected_html

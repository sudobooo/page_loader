import os
import requests_mock
from tempfile import TemporaryDirectory

from page_loader.page_downloader import download
from page_loader.url_converter import convert


URL = 'https://ru.hexlet.io/courses'
URL_IMAGE = 'https://ru.hexlet.io/assets/professions/nodejs.png'
EXPECTED_CONVERT_URL = 'ru-hexlet-io-courses.html'


def get_path(path_, name):
    return os.path.join('tests', path_, name)


def get_content(file):
    with open(file, 'rb') as file:
        return file.read()


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


raw = read(get_path('fixtures', 'raw.html'))
expected_html = read(get_path('fixtures', 'expected.html'))
image = get_content(get_path('fixtures', 'image.png'))


def test_convert_url():

    actual = convert(URL)
    assert actual == EXPECTED_CONVERT_URL


def test_dowloads():

    with requests_mock.Mocker() as m, TemporaryDirectory() as tmpdir:
        m.get(URL, text=raw)
        m.get(URL_IMAGE, content=image)

        expected_path = get_path(tmpdir, EXPECTED_CONVERT_URL)
        actual_path = download(URL, tmpdir)
        assert actual_path == expected_path

        actual_file = read(actual_path)
        assert actual_file == expected_html

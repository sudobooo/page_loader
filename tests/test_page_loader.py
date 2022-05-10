import os
import requests_mock
from tempfile import TemporaryDirectory

from page_loader.page_downloader import download
from page_loader.url_converter import convert


def get_path(path_, name):
    return os.path.join('tests', path_, name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


URL = 'https://ru.hexlet.io/courses'
EXPECTED_CONVERT_URL = 'ru-hexlet-io-courses.html'
EXPECTED_DOWNLOAD = read(get_path('fixtures', 'expected_result.html'))


def test_convert_url():

    actual = convert(URL)
    assert actual == EXPECTED_CONVERT_URL


def test_dowloads():

    with requests_mock.Mocker() as m, TemporaryDirectory() as tmpdir:
        m.get(URL, text=EXPECTED_DOWNLOAD)

        expected_path = get_path(tmpdir, EXPECTED_CONVERT_URL)
        actual_path = download(tmpdir, URL)
        assert actual_path == expected_path

        actual_file = read(actual_path)
        assert actual_file == EXPECTED_DOWNLOAD

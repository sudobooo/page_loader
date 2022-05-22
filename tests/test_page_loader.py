import os
import requests_mock
import pytest
from tempfile import TemporaryDirectory

from page_loader.page_downloader import download
from page_loader.url_converter import convert


URL = 'https://ru.hexlet.io'
URL_IMG = 'https://ru.hexlet.io/professions/python.png'

RAW = 'tests/fixtures/raw.html'
IMG = 'tests/fixtures/image.png'
RESULT_HTML = 'tests/fixtures/expected.html'

DIRECTORY = 'ru-hexlet-io_files'
EXPECTED_HTML = 'ru-hexlet-io.html'
EXPECTED_IMG = os.path.join(DIRECTORY, 'ru-hexlet-io-professions-python.png')


def get_content(file):
    with open(file, 'rb') as file:
        return file.read()


def read(file):
    with open(file, 'r') as f:
        return f.read()


@pytest.mark.parametrize('url, expected, type', [
    (
        'https://ru.hexlet.io',
        'ru-hexlet-io.html',
        'html'
    ),
    (
        'https://ru.hexlet.io/professions/python.js',
        'ru-hexlet-io-professions-python.js',
        None
    ),
    (
        'https://ru.hexlet.io/professions',
        'ru-hexlet-io-professions_files',
        'dir'
    )
])
def test_convert_url(url, expected, type):

    actual = convert(url, type)
    assert actual == expected


def test_dowloads():
    html_raw = get_content(RAW).decode()
    html_expected = read(RESULT_HTML)
    image = get_content(IMG)

    with requests_mock.Mocker() as m, TemporaryDirectory() as tmpdir:
        m.get(URL, text=html_raw)
        m.get(URL_IMG, content=image)
        download(URL, tmpdir)

        html_path = os.path.join(tmpdir, EXPECTED_HTML)
        img_path = os.path.join(tmpdir, EXPECTED_IMG)

        actual_html = read(html_path)
        assert actual_html == html_expected

        actual_img = get_content(img_path)
        assert actual_img == image

        actual_path = os.path.join(tmpdir, DIRECTORY)
        assert len(os.listdir(actual_path)) == 1

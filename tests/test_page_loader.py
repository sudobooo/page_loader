import os
import requests_mock
import pytest
from tempfile import TemporaryDirectory

from page_loader.page_downloader import download
from page_loader.url_converter import convert


URL = 'https://ru.hexlet.io'
URL_IMG = 'https://ru.hexlet.io/professions/python.png'
URL_CSS = 'https://ru.hexlet.io/assets/application.css'
URL_JS = 'https://ru.hexlet.io/packs/js/runtime.js'

RAW = 'tests/fixtures/raw.html'
IMG = 'tests/fixtures/image.png'
HTML = 'tests/fixtures/expected.html'
CSS = 'tests/fixtures/styles.css'
JS = 'tests/fixtures/script.js'

DIRECTORY = 'ru-hexlet-io_files'
EXPECTED_HTML = 'ru-hexlet-io.html'
EXPECTED_IMG = os.path.join(DIRECTORY, 'ru-hexlet-io-professions-python.png')
EXPECTED_CSS = os.path.join(DIRECTORY, 'ru-hexlet-io-assets-application.css')
EXPECTED_JS = os.path.join(DIRECTORY, 'ru-hexlet-io-packs-js-runtime.js')


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
    html_raw = read(RAW)
    html_expected = read(HTML)
    image = get_content(IMG)
    css = get_content(CSS)
    js = get_content(JS)

    with requests_mock.Mocker() as m, TemporaryDirectory() as tmpdir:
        m.get(URL, text=html_raw)
        m.get(URL_IMG, content=image)
        m.get(URL_CSS, content=css)
        m.get(URL_JS, content=js)
        download(URL, tmpdir)

        html_path = os.path.join(tmpdir, EXPECTED_HTML)
        img_path = os.path.join(tmpdir, EXPECTED_IMG)
        css_path = os.path.join(tmpdir, EXPECTED_CSS)
        js_path = os.path.join(tmpdir, EXPECTED_JS)

        actual_html = read(html_path)
        assert actual_html == html_expected

        actual_img = get_content(img_path)
        assert actual_img == image

        actual_css = get_content(css_path)
        assert actual_css == css

        actual_js = get_content(js_path)
        assert actual_js == js

        actual_path = os.path.join(tmpdir, DIRECTORY)
        assert len(os.listdir(actual_path)) == 3

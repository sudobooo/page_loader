import os
import requests_mock
from tempfile import TemporaryDirectory

from page_loader.page_downloader import download
from page_loader.url_converter import convert


URL = 'https://ru.hexlet.io/courses'
URL_IMG = 'https://ru.hexlet.io/assets/professions/python.png'

RAW = 'tests/fixtures/raw.html'
IMG = 'tests/fixtures/image.png'
RESULT_HTML = 'tests/fixtures/expected.html'

DIRECTORY = 'ru-hexlet-io-courses_files'
EXPECTED_HTML = 'ru-hexlet-io-courses.html'
EXPECTED_IMG = os.path.join(DIRECTORY,
                            'ru-hexlet-io-assets-professions-python.png')


def get_content(file):
    with open(file, 'rb') as file:
        return file.read()


def read(file):
    with open(file, 'r') as f:
        return f.read()


def test_convert_url():

    actual = convert(URL)
    assert actual == EXPECTED_HTML


def test_dowloads():
    html_code = get_content(RAW).decode()
    html_result = read(RESULT_HTML)
    image = get_content(IMG)

    with requests_mock.Mocker() as m, TemporaryDirectory() as tmpdir:
        m.get(URL, text=html_code)
        m.get(URL_IMG, content=image)
        download(URL, path_to_dir=tmpdir)

        path_to_html = os.path.join(tmpdir, EXPECTED_HTML)
        path_to_img = os.path.join(tmpdir, EXPECTED_IMG)

        result_html = get_content(path_to_html).decode()
        assert result_html == html_result

        result_img = get_content(path_to_img)
        assert result_img == image

        path = os.path.join(tmpdir, DIRECTORY)
        assert len(os.listdir(path)) == 1

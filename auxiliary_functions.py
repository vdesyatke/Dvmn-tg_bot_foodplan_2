import os
from urllib import parse
from pathlib import Path
import requests


def extract_file_extension_from_path(path):
    return os.path.splitext(path)[1]


def extract_file_extension_from_url(url):
    path = parse.urlsplit(url).path
    return extract_file_extension_from_path(path)


def extract_file_basename_from_url(url):
    path = parse.urlsplit(url).path
    quoted_basename = os.path.split(path)[1]
    return parse.unquote(quoted_basename)


def download_pic(url, path, params=None):
    path_to_folder = os.path.dirname(path)
    Path(path_to_folder).mkdir(parents=True, exist_ok=True)

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)

import os
from urllib import parse


def extract_file_extension_from_path(path):
    return os.path.splitext(path)[1]


def extract_file_extension_from_url(url):
    path = parse.urlsplit(url).path
    return extract_file_extension_from_path(path)


def extract_file_basename_from_url(url):
    path = parse.urlsplit(url).path
    quoted_basename = os.path.split(path)[1]
    return parse.unquote(quoted_basename)

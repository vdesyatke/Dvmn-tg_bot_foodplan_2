import requests
from auxiliary_functions import extract_file_extension_from_url, download_pic
from environs import Env
import argparse


def create_parser():
    description = 'Download APOD NASA photos'
    parser = argparse.ArgumentParser(description=description)
    h = 'Quantity of photos to download'
    parser.add_argument('-c', '--count', type=int, help=h, default=30)
    return parser


def main():
    env = Env()
    env.read_env()

    parser = create_parser()
    count = parser.parse_args().count

    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': env('NASA_API_KEY'), 'count': count}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        if image['media_type'] != 'image':
            continue
        url = image['url']
        ext = extract_file_extension_from_url(url)
        path = f'images/nasa_apod_{number}{ext}'
        download_pic(url=url, path=path)


if __name__ == '__main__':
    main()

import os
import requests
import auxiliary_functions
from environs import Env
from datetime import date, datetime
from pathlib import Path


def download_pic(url, path, params=None):
    path_to_folder = os.path.dirname(path)
    Path(path_to_folder).mkdir(parents=True, exist_ok=True)

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_apod_images(count=30):
    env = Env()
    env.read_env()

    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': env('NASA_API_KEY'), 'count': count}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    if not os.path.exists('images'):
        os.makedirs('images')

    for number, image in enumerate(response.json()):
        if image['media_type'] == 'image':
            url = image['url']
            ext = auxiliary_functions.extract_file_extension_from_url(url)
            path = f'images/nasa_apod_{number}{ext}'
            download_pic(url=url, path=path)


def fetch_epic_images(count=10):
    env = Env()
    env.read_env()

    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    payload = {'api_key': env('NASA_API_KEY')}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    valid_dates = (x['date'] for x in response.json()[:count])

    number_of_images = 0
    for dt in valid_dates:
        url = f'https://api.nasa.gov/EPIC/api/natural/{dt}'
        response = requests.get(url, params=payload)
        response.raise_for_status()

        dt = datetime.strptime(dt, '%Y-%m-%d')
        dt = dt.strftime('%Y/%m/%d')

        for image in response.json():
            basename = image['image']
            url = f'https://api.nasa.gov/EPIC/archive/natural/{dt}/png/{basename}.png'
            download_pic(url=url, path=f'images/{basename}.png', params=payload)
            number_of_images += 1
            if number_of_images == count:
                break

        if number_of_images == count:
            break

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()

    images = response.json()['links']['flickr']['original']

    if not images:
        url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
        response = requests.get(url)
        response.raise_for_status()
        images = response.json()['links']['flickr']['original']

    for number, image in enumerate(images):
        ext = auxiliary_functions.extract_file_extension_from_url(image)
        download_pic(image, f'images/space_{number}{ext}')


def main():
    # fetch_spacex_last_launch()
    # fetch_apod_images(count=2)
    # fetch_epic_images(count=2)


if __name__ == '__main__':
    main()

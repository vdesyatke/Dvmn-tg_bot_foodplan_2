import requests
from auxiliary_functions import download_pic
from environs import Env
import argparse
from datetime import datetime


def create_parser():
    description = 'Download NASA EPIC photos'
    parser = argparse.ArgumentParser(description=description)
    h = 'Quantity of photos to download'
    parser.add_argument('-c', '--count', type=int, help=h, default=10)
    return parser


def main():
    env = Env()
    env.read_env()

    parser = create_parser()
    count = parser.parse_args().count

    url = 'https://epic.gsfc.nasa.gov/api/natural/all'
    payload = {'api_key': env('NASA_API_KEY')}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    valid_dates = (x['date'] for x in response.json())

    number_of_images = 0
    for valid_date in valid_dates:
        url = f'https://epic.gsfc.nasa.gov/api/natural/date/{valid_date}'
        response = requests.get(url, params=payload)
        response.raise_for_status()

        valid_date = datetime.strptime(valid_date, '%Y-%m-%d')
        valid_date = valid_date.strftime('%Y/%m/%d')

        for image in response.json():
            basename = image['image']
            url = f'https://epic.gsfc.nasa.gov/archive/natural/{valid_date}' \
                  f'/png/{basename}.png'
            try:
                download_pic(
                    url=url,
                    path=f'images/{basename}.png',
                    params=payload
                )
                number_of_images += 1
            except requests.exceptions.HTTPError:
                print(f'Failed to download {url}, trying next...')
            if number_of_images == count:
                break

        if number_of_images == count:
            break


if __name__ == '__main__':
    main()

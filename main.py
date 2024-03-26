import os
import requests


def return_file_extension(path):
    return os.path.basename(path).split('.')[-1]


def download_pic(url, path):
    path_to_folder = os.path.dirname(path)
    if not os.path.exists(path_to_folder):
        os.makedirs(path_to_folder)

    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()

    images = response.json()['links']['flickr']['original']

    for image in images:
        filename = os.path.basename(image)
        download_pic(image, f'images/{filename}')


def main():
    # if not os.path.exists('images'):
    #     os.makedirs('images')
    # fetch_spacex_last_launch()


if __name__ == '__main__':
    main()

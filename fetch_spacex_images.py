from auxiliary_functions import extract_file_extension_from_url, download_pic
import argparse
import requests


def create_parser():
    description = 'Download photos of SpaceX launches'
    parser = argparse.ArgumentParser(description=description)
    h = 'ID of launch'
    parser.add_argument('-id', '--launch_id', help=h, default='latest')
    return parser


def is_valid_launch_id(launch_id):
    """Checks if the given id is a valid SpaceX launch id"""
    url = 'https://api.spacexdata.com/v5/launches'
    response = requests.get(url)
    response.raise_for_status()
    launch_id_list = (launch['id'] for launch in response.json())
    return launch_id in launch_id_list


def return_id_of_latest_photographed_launch():
    """Returns id of the latest photographed SpaceX launch"""
    url = 'https://api.spacexdata.com/v5/launches'
    response = requests.get(url)
    response.raise_for_status()
    for launch in response.json()[::-1]:
        if launch['links']['flickr']['original']:
            return launch['id']


def main():
    parser = create_parser()
    launch_id = parser.parse_args().launch_id
    if launch_id == 'latest':
        launch_id = return_id_of_latest_photographed_launch()

    if not is_valid_launch_id(launch_id):
        print(f'{launch_id} is not a valid SpaceX launch id')
        return None

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    images = response.json()['links']['flickr']['original']

    if not images:
        print(f'No photos provided for the launch {launch_id}')
    else:
        for number, image in enumerate(images):
            ext = extract_file_extension_from_url(image)
            download_pic(image, f'images/space_{number}{ext}')


if __name__ == '__main__':
    main()

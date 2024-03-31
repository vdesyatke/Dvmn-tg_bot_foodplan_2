import random
from environs import Env
import telegram
import argparse
import os


TG_FILESIZE_LIMIT = 20 * 1024 * 1024


def create_parser():
    description = 'Publish photo'
    parser = argparse.ArgumentParser(description=description)
    help = 'filename to publish'
    parser.add_argument('-f', '--filename', type=str, help=help)
    return parser


def publish_photo(bot, chat_id, filename):
    """Posts specified photo from 'images' folder to telegram channel"""
    file = os.path.join('images/', filename)
    if os.path.getsize(file) > TG_FILESIZE_LIMIT:
        print('File is too heavy. Only files less than 20MB are accepted')
        return
    bot.send_photo(chat_id=chat_id, photo=open(file, 'rb'))


def main():
    env = Env()
    env.read_env()

    parser = create_parser()
    filename = parser.parse_args().filename

    bot = telegram.Bot(token=env('TG_TOKEN'))
    chat_id = env('TG_CHAT_ID')

    if not filename:
        filename = random.choice(
            tuple(os.walk('images'))[0][2]
        )

    try:
        publish_photo(bot=bot, chat_id=chat_id, filename=filename)
    except FileNotFoundError:
        print(f'File {filename} not found in "images/" folder')


if __name__ == '__main__':
    main()

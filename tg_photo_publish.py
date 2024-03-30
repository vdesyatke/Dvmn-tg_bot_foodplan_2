import random
from environs import Env
import telegram
import argparse
import os


def create_parser():
    description = 'Publish photo'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f', '--filename', type=str, help='filename to publish')
    return parser


def publish_photo(bot, chat_id, filename):
    """Posts specified photo from folder 'images' to telegram channel"""
    TG_FILESIZE_LIMIT = 20 * 1024 * 1024
    try:
        if os.path.getsize(
                os.path.join('images/', filename)
        ) > TG_FILESIZE_LIMIT:
            print('File is too heavy. Only files less than 20MB are accepted')
        else:
            bot.send_photo(
                chat_id=chat_id,
                photo=open(os.path.join('images/', filename), 'rb')
            )
    except FileNotFoundError:
        print(f'File {filename} not found in "images/" folder')


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
    publish_photo(bot=bot, chat_id=chat_id, filename=filename)


if __name__ == '__main__':
    main()

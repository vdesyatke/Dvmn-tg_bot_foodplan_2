import random
from environs import Env
import telegram
import argparse
import time
import os


def create_parser():
    description = 'Delayed publish'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-d', '--hours_delay', type=float, help='Delay in hours', default=4)
    return parser


def publish_with_delay(bot, chat_id, delay):
    TG_FILESIZE_LIMIT = 20 * 1024 * 1024
    dirpath, _, filenames = next(os.walk('images'))
    assert filenames
    while True:
        for filename in filenames:
            if os.path.getsize(os.path.join(dirpath, filename)) > TG_FILESIZE_LIMIT:
                continue
            try:
                bot.send_photo(chat_id=chat_id, photo=open(os.path.join(dirpath, filename), 'rb'))
                time.sleep(delay * 3600)
            except FileNotFoundError:
                pass
        random.shuffle(filenames)


def main():
    env = Env()
    env.read_env()

    parser = create_parser()
    delay = parser.parse_args().hours_delay

    bot = telegram.Bot(token=env('TG_TOKEN'))
    chat_id = bot.get_updates()[-1].message.chat_id

    publish_with_delay(bot=bot, chat_id=chat_id, delay=delay)


if __name__ == '__main__':
    main()

from environs import Env
import telegram


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TG_TOKEN'))
    print(bot.get_me())

    chat_id = bot.get_updates()[-1].message.chat_id

    bot.send_message(chat_id=chat_id, text="Test message")


if __name__ == '__main__':
    main()
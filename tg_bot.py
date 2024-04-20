from environs import Env
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipes.recipes.settings")
django.setup()

from recipes.dishes import models


# Функция для получения случайного блюда
def get_random_dish():
    random_dish = models.Dishes.objects.order_by('?').first()  # Получаем случайное блюдо
    return random_dish


def publish_recipe(bot, chat_id, dish):
    """Опубликовать рецепт

    Публикует в таком порядке:
    - название рецепта
    - время приготовления
    - фото
    - рецепт
    - список ингредиентов
    """
    bot.send_message(chat_id=chat_id, message=dish.name)
    bot.send_message(chat_id=chat_id,
                     message=f'Время приготовления {dish.cooktime} мин'
                     )
    with open(dish.image, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)
    bot.send_message(chat_id=chat_id, message=dish.ingredients)
    bot.send_message(chat_id=chat_id, message=dish.recipe)
    # file = os.path.join('images/', filename)
    # if os.path.getsize(file) > TG_FILESIZE_LIMIT:
    #     print('File is too heavy. Only files less than 20MB are accepted')
    #     return
    # with open(file, 'rb') as photo:
    #     bot.send_photo(chat_id=chat_id, photo=photo)


def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Random", callback_data='random'),
         InlineKeyboardButton("Another", callback_data='another')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


# Обработчик нажатия на кнопку
def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'random':
        # query.edit_message_text(text="You chose: Random")
        dish = get_random_dish()
        if dish:
            query.edit_message_text(text=dish.name)
            query.bot.send_photo(chat_id=query.message.chat_id, photo=dish.image)
        else:
            query.edit_message_text(text="No random dish available")
    elif query.data == 'another':
        query.edit_message_text(text="You chose: Another")


def main():
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TG_TOKEN'))
    chat_id = env('TG_CHAT_ID')

    updater = Updater(env('TG_TOKEN'), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

    # try:
    #     publish_photo(bot=bot, chat_id=chat_id, filename=filename)
    # except FileNotFoundError:
    #     print(f'File {filename} not found in "images/" folder')


if __name__ == '__main__':
    main()

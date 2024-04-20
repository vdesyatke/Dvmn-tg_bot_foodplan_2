from environs import Env
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipes.settings")
django.setup()

from dishes import models # noqa E402


# Функция для получения случайного блюда
def get_random_dish():
    random_dish = models.Dishes.objects.order_by('?').first()  # Получаем случайное блюдо
    return random_dish


def publish_recipe(query, chat_id, dish):
    """Опубликовать рецепт

    Публикует в таком порядке:
    - название рецепта
    - время приготовления
    - фото
    - рецепт
    - список ингредиентов
    """
    query.bot.send_message(chat_id=chat_id, text=dish.name)
    query.bot.send_message(chat_id=chat_id, text='Запускаю publish...')
    query.bot.send_message(chat_id=chat_id,
                     text=f'Время приготовления {dish.cooktime} мин'
                     )
    with open(dish.images, 'rb') as photo:
        query.bot.send_photo(chat_id=chat_id, photo=photo)
    query.bot.send_message(chat_id=chat_id, text=f'Ингредиенты:{dish.ingredients}')
    query.bot.send_message(chat_id=chat_id, text=f'Рецепт: + {dish.recipe}')


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
        dish = get_random_dish()
        if dish:
            chat_id = query.message.chat_id
            query.edit_message_text(text=dish.name)
            query.bot.send_message(chat_id=chat_id,
                                   text=f'Время приготовления {dish.cooktime} мин'
                                   )
            query.bot.send_photo(chat_id=chat_id, photo=dish.images)
            query.bot.send_message(chat_id=chat_id, text=f'Ингредиенты:\n{dish.ingredients}')
            query.bot.send_message(chat_id=chat_id, text=f'Рецепт:\n{dish.recipe}')

            # publish_recipe(query=query, chat_id=query.message.chat_id, dish=dish)
            # query.edit_message_text(text=dish.name)
            # query.bot.send_photo(chat_id=query.message.chat_id, photo=dish.images)
            # query.bot.send_message(chat_id=query.message.chat_id, text=dish.cooktime)

        else:
            query.edit_message_text(text="No random dish available")
    elif query.data == 'another':
        query.edit_message_text(text="You chose: Another")


def main():
    env = Env()
    env.read_env()

    updater = Updater(env('TG_TOKEN'), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# Dvmn-tg_bot_Foodplan
Это телеграм бот, который по запросу присылает "рецепт на каждый день"

## Installation
0. You need python interpreter installed on your PС. The project is tested on Python 3.10.
1. Clone the project to your PC, details [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Install, run and activate your virtual environment, details [here](https://docs.python-guide.org/dev/virtualenvs/).
3. To install the dependencies, simply run 
```python
pip install -r requirements.txt
```

5. Следуй этим [инструкциям](https://sitogon.ru/blog/252-kak-sozdat-telegram-bot-poluchit-ego-token-i-chat-id) чтобы создать новый телеграм бот, сгенерировать свой телеграм токен и получить Chat ID вашего телеграм-канала.
6. В корневой директории вашего проекта создай новый файл `.env` с переменными среды:
```
TG_TOKEN={your_telegram_token}
TG_CHAT_ID={your_chat_id}
```

## Скрипты
### tg_photo_publish.py
Posts a photo to telegram channel

### tg_scheduled_photo_publish.py
Posts photos to telegram channel on schedule

## Примеры использования

## License
This software is licensed under the MIT License - see the [LICENSE](https://github.com/vdesyatke/Dvmn-Weather/blob/master/LICENSE) file for details

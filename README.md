# Dvmn-Space_photos
This program downloads space photos from the following sources: [SpaceX launches](https://docs.spacexdata.com/), [NASA APOD](https://apod.nasa.gov/apod/), [NASA EPIC](https://epic.gsfc.nasa.gov/).

## Installation
0. You need python interpreter installed on your PС. The project is tested on Python 3.10.
1. Clone the project to your PC, details [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Install, run and activate your virtual environment, details [here](https://docs.python-guide.org/dev/virtualenvs/).
3. To install the dependencies, simply run 
```python
pip install -r requirements.txt
```
4. Generate your NASA API key [here](https://api.nasa.gov/) 
5. Follow [instructions](https://sitogon.ru/blog/252-kak-sozdat-telegram-bot-poluchit-ego-token-i-chat-id) to create a new telegram bot, generate your telegram token and retrieve Chat ID of your telegram channel.
6. In the root directory of the project create a new file named `.env` with the environment variables:
```
NASA_API_KEY={your_NASA_API_key}
TG_TOKEN={your_telegram_token}
TG_CHAT_ID={your_chat_id}
```

## Scripts
### fetch_spacex_images
Downloads photos of SpaceX launches

### fetch_nasa_apod_images
Downloads NASA APOD photos

### fetch_nasa_epic_images
Downloads NASA EPIC photos

### tg_photo_publish.py
Posts a photo to telegram channel

### tg_scheduled_photo_publish.py
Posts photos to telegram channel on schedule

## Examples of use

### Download photos of the latest photographed SpaceX launch
```python
python fetch_spacex_images.py
```
This will create a new folder 'images/', if not exists, in your root directory, and download photos into it.

### Download photos of SpaceX launch with specific ID
```python
python fetch_spacex_images.py -id 6243adcaaf52800c6e919254
```

### Download 30 (default) NASA APOD images
```python
python fetch_nasa_apod_images.py
```

### Download specified amount of NASA APOD images
```python
python fetch_nasa_apod_images.py -c 10
```

### Download 10 (default) NASA EPIC images
```python
python fetch_nasa_epic_images.py
```

### Download specified amount of NASA EPIC images
```python
python fetch_nasa_epic_images.py -c 5
```

### Automatically post images one by one with specified hour delay
```python
python tg_scheduled_photo_publish.py -d 1
```
The script posts all images from the 'images/' folder with specified delay, then shuffles them and repeats until manually interrupted.
The folder must be non-empty.
Files over 20MB will be ignored. Default delay is 4 hours.

### Post specified or random file
```python
python tg_photo_publish.py -f space_0.jpg
```
Posts specified image from the 'images/' folder. If no filename provided, posts random image from 'images/' folder. 

## License
This software is licensed under the MIT License - see the [LICENSE](https://github.com/vdesyatke/Dvmn-Weather/blob/master/LICENSE) file for details

import requests
import pprint
from PIL import Image
import glob
import os
import sys
import time
from io import open
from instabot import Bot
from os import listdir
from dotenv import load_dotenv
import os.path
from pathlib import Path


def download_picture(url):
    filename = Path('images', 'hubble.jpg')
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(url)
    response.raise_for_status()
    spacex_pictures = response.json()['links']['flickr_images']

    for picture_number, picture in enumerate(spacex_pictures):
        file_with_picture = Path('images', 'spacex{}.jpg'.format(picture_number))
        response = requests.get(spacex_pictures[picture_number])

        with open(file_with_picture, 'wb') as file:
            file.write(response.content)


def download_hubble_pictures(id_image):
    url = "http://hubblesite.org/api/v3/image/" + id_image
    response = requests.get(url)
    response.raise_for_status()
    hubble_pictures = response.json()['image_files']

    for picture in hubble_pictures:
        link = picture['file_url']
        url = "https:" + link
        split_pictures = link.split('.')
        filename = Path('images', 'hubble{}.{}'.format(id_image, split_pictures[-1]))
        response = requests.get(url)
        response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def download_hubble_collection(collection):
    url = "http://hubblesite.org/api/v3/images/" + collection
    response = requests.get(url)
    response.raise_for_status()
    hubble_collection = response.json()

    for picture in hubble_collection:
        image_id = picture['id']
        url = f"http://hubblesite.org/api/v3/image/{image_id}"
        response = requests.get(url)
        response.raise_for_status()
        hubble_collection = response.json()['image_files']

        for picture in hubble_collection:
            link = picture['file_url']
            url = "https:" + link
            filename = Path('collection', 'hubble-{}-{}.jpg'.format(collection, image_id))
            response = requests.get(url)
            response.raise_for_status()

            with open(filename, 'wb') as file:
                file.write(response.content)


def main():
    os.chdir("C:/Users/mokko/Desktop/space-bot/space-pictures")
    load_dotenv()
    download_picture("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg")
    download_hubble_pictures("1")
    #download_hubble_collection("spacecraft")
    fetch_spacex_last_launch()

    insta_login = os.getenv("LOGIN")
    insta_password = os.getenv("PASSWORD")
    bot = Bot()
    bot.login(username=insta_login, password=insta_password)

    pictures_to_instagram = []

    for file_name in os.walk(Path('images')):
        pictures_to_instagram.append(file_name)

    for file_name in os.walk(Path('collection')):
        pictures_to_instagram.append(file_name)

    for address, dirs, file_names in pictures_to_instagram:
        for file_name in file_names:
            instagram_image = Image.open(os.path.join(address, file_name))
            instagram_image.thumbnail((1080, 1080))
            instagram_image.save(os.path.join(address, file_name))
            bot.upload_photo(os.path.join(address, file_name))


if __name__ == '__main__':
    main()


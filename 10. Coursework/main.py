import json
import os
import requests
import yadisk
from vk_api import VkApi
from tqdm import tqdm
import logging

class VKPhotosDownloader:
    def __init__(self, vk_token, yandex_token):
        self.vk_session = VkApi(token=vk_token)
        self.vk = self.vk_session.get_api()
        self.yandex = yadisk.YaDisk(yandex_token)
        self.likes_limit = 5

        logging.basicConfig(filename='app.log', level=logging.INFO)

    def download_photos(self, user_id):
        photos = self.vk.photos.get(owner_id=user_id, album_id='profile', extended=1, count=self.likes_limit)
        photos_info = []
        for photo in tqdm(photos['items'], desc="Downloading photos"):
            max_size = max(photo['sizes'], key=lambda x: x['width'] * x['height'])
            likes = photo['likes']['count']
            file_name = f"{likes}.jpg"
            url = max_size['url']
            response = requests.get(url)
            with open(file_name, 'wb') as f:
                f.write(response.content)
            self.yandex.upload(file_name, f"VKPhotos/{file_name}")
            os.remove(file_name)
            photos_info.append({
                "file_name": file_name,
                "size": max_size['type']
            })
            logging.info(f"Downloaded photo {file_name}")
        with open('photos_info.json', 'w') as f:
            json.dump(photos_info, f, indent=4)

if __name__ == '__main__':
    vk_token = input("Введите токен VK: ")
    yandex_token = input("Введите токен Яндекс.Диска: ")
    user_id = input("Введите ID пользователя VK: ")
    downloader = VKPhotosDownloader(vk_token, yandex_token)
    downloader.download_photos(user_id)


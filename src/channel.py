import json
import os
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv(Path(__file__).parent.parent.joinpath("data").joinpath(".env"))
api_key: str = os.environ.get('API_KEY_YOUTUBE')


class Channel:
    """Класс для ютуб-канала"""
    __channel_id = ''

    def __init__(self, channel_id: str) -> None:

        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        """получаю словарь с информацией о канале"""
        request = self.get_info_channel()
        result = request["items"][0]

        """инициализирую поля через полученный словарь"""
        self.name: str = result["kind"]
        self.title: str = result["snippet"]["title"]
        self.url: str = result["snippet"]["thumbnails"]["default"]["url"]
        self.count_subscribers: str = result["statistics"]["subscriberCount"]
        self.video_count: str = result["statistics"]["videoCount"]
        self.views: str = result["statistics"]["viewCount"]

    def __str__(self):
        """Возвращаем информацию для пользователя"""
        return f"{self.title} {self.url}"

    def __add__(self, other):
        """Сложение по просмотрам"""
        return int(self.views) + int(other.views)

    def __sub__(self, other):
        """Вычитание по просмотрам"""
        return int(self.views) - int(other.views)

    def __lt__(self, other):
        """Сравнение классов по просмотрам"""
        return self.views < other.views

    def __le__(self, other):
        """Сравнение классов по просмотрам"""
        return self.views <= other.views

    def __gt__(self, other):
        """Сравнение классов по просмотрам"""
        return self.views > other.views

    def __ge__(self, other):
        """Сравнение классов по просмотрам"""
        return self.views >= other.views

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        request = self.get_info_channel()
        print(json.dumps(request, indent=2, ensure_ascii=False))

    @property
    def channel(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        youtube = build("youtube", "v3", developerKey=api_key)

        return youtube

    def get_info_channel(self):
        """Получаем информацию о канале"""
        youtube = self.get_service()
        result = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        """Возвращаем в виде словаря"""
        return result

    def to_json(self, way) -> None:
        """Создали шаблон json для сохранения информации в json файл"""
        j_list = {
            "id": self.__channel_id,
            "name": self.name,
            "title": self.title,
            "url": self.url,
            "subscriberCount": self.count_subscribers,
            "viewCount": self.views
        }
        """считываем весь список в json файле"""
        with open(way, "r", encoding='utf8') as file:
            res = json.load(file)
            res.append(j_list)
        """добавляем в считанный список новые данные и перезаписываем json файл"""
        with open(way, 'w', encoding='utf8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv(Path(__file__).parent.parent.joinpath("data").joinpath(".env"))
api_key: str = os.environ.get('API_KEY_YOUTUBE')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        result = request["items"][0]

        self.name: str = result["kind"]
        self.title: str = result["snippet"]["title"]
        self.url: str = result["snippet"]["thumbnails"]["default"]["url"]
        self.count_subscribers: int = result["statistics"]["subscriberCount"]
        self.video_count: int = result["statistics"]["videoCount"]
        self.views: int = result["statistics"]["viewCount"]

    def __str__(self):
        return f"{self.title} {self.url}"

    def __add__(self, other):
        return int(self.views) + int(other.views)

    def __sub__(self, other):
        return int(self.views) - int(other.views)

    def __lt__(self, other):
        return self.views < other.views

    def __le__(self, other):
        return self.views <= other.views

    def __gt__(self, other):
        return self.views > other.views

    def __ge__(self, other):
        return self.views >= other.views

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(request, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls

    def to_json(self, way) -> None:
        j_list = {
            "id": self.channel_id,
            "name": self.name,
            "title": self.title,
            "url": self.url,
            "subscriberCount": int(self.count_subscribers),
            "viewCount": int(self.views)
        }

        with open(way, "r", encoding='utf8') as file:
            res = json.load(file)
            res.append(j_list)
        with open(way, 'w', encoding='utf8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)

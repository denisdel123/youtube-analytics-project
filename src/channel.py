import os
from googleapiclient.discovery import build
value = os.getenv("API_KEY_YOUTUBE")


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = build("youtube", "v3", developerKey=value)
        request = youtube.vidios().list(part="snippet,contentDetails", id=self.channel_id)
        response = request.execute()
        print(response)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pass

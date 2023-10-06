import re
from datetime import datetime
from datetime import timedelta

import os
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv(Path(__file__).parent.parent.joinpath("data").joinpath(".env"))
api_key: str = os.environ.get('API_KEY_YOUTUBE')


class PlayList:

    def __init__(self, _id_):

        """инициализируем _id_ и создаем объект для работы с API youtube"""
        self._id_ = _id_
        self.youtube = build("youtube", "v3", developerKey=api_key)

        """обращаемся к плейлисту по id, присваиваем полям url title значения"""
        play_list_info = self.get_info_playlist_to_id()
        self.title = play_list_info["snippet"]["title"]
        self.url = f"https://www.youtube.com/playlist?list={_id_}"

    @property
    def total_duration(self):

        all_time = []
        sum_time = timedelta()
        video_response = self.get_id_video()

        for item in video_response['items']:
            time = item['contentDetails']['duration']

            """считываем время и записываем его в список через модуль re"""
            match = re.match(r'PT(\d+H)?(\d+M)?(\d+S)?', time)
            hours = int(match.group(1)[:-1]) if match.group(1) else 0
            minutes = int(match.group(2)[:-1]) if match.group(2) else 0
            seconds = int(match.group(3)[:-1]) if match.group(3) else 0

            """преобразуем полученные данные времени в timedelta и записываем в отдельный список"""
            corr_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            all_time.append(corr_time)

            """суммируем все время, записываем длительность всех роликов и возвращаем"""
        for time in all_time:
            sum_time += time

        return sum_time

    def show_best_video(self):
        dict_like = {}
        likes_count: int
        id_video = ''

        video_response = self.get_id_video()

        for video in video_response["items"]:
            dict_like[video["id"]] = video['statistics']['likeCount']

        for k, i in dict_like.items():
            likes_count = i
            id_video = k
            if likes_count < i:
                id_video = k

        url_video = f"https://youtu.be/{id_video}"

        return url_video

    def get_info_for_playlist(self):
        """получаем данные по видеороликам в плейлисте"""
        play_list = self.youtube.playlistItems().list(playlistId=self._id_,
                                                      part='contentDetails',
                                                      maxResults=50,
                                                      ).execute()
        return play_list

    def get_id_video(self):
        play_list = self.get_info_for_playlist()
        """получаеа id каждого видео и выводим в список"""
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in play_list['items']]

        """выводим информацию о видеороликах по id"""
        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()

        return video_response

    def get_info_playlist_to_id(self):
        play_list_info = self.youtube.playlists().list(id=self._id_, part='snippet', ).execute()
        result = play_list_info["items"][0]
        return result

import os
from pathlib import Path

from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.joinpath("data").joinpath(".env"))
api_key: str = os.environ.get('API_KEY_YOUTUBE')


class Video:

    def __init__(self, id_video):
        try:
            youtube = build("youtube", "v3", developerKey=api_key)
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=id_video
                                                   ).execute()
            result = video_response["items"][0]
            self.id_video = id_video
            self.title = str(result["snippet"]['title'])
            self.url_video = str(result["snippet"]['thumbnails']["default"]["url"])
            self.views_video = result['statistics']['viewCount']
            self.like_count = str(result['statistics']['likeCount'])
        except IndexError:
            print("IndexError")
            self.id_video = id_video
            self.title = None
            self.views_video = None
            self.like_count = None

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):

    def __init__(self, id_video, id_play):
        super().__init__(id_video)
        self.id_play = id_play

    def __str__(self):
        return f"{self.title}"

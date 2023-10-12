import datetime

import pytest
from src.channel import Channel
from src.video import Video, PLVideo
from src.playlist import PlayList


@pytest.fixture()
def channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture()
def channel2():
    return Channel('UCwHL6WHUarjGfUM_586me8w')


def test_str(channel):
    assert str(channel) == (
        'MoscowPython https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s88-c-k-c0x00ffffff-no-rj'
    )


def test_add(channel, channel2):
    channel.views = 55000
    channel2.views = 58000
    assert channel + channel2 == 113000


def test_lt(channel, channel2):
    channel.views = 50000
    channel2.views = 54000
    assert channel - channel2 == -4000
    assert channel2 - channel == 4000


def test_le_lt(channel, channel2):
    channel.views = 100
    channel2.views = 50
    assert channel > channel2
    channel.views = 100
    channel2.views = 100
    assert channel >= channel2
    channel.views = 50
    channel2.views = 60
    assert channel < channel2
    channel.views = 50
    channel2.views = 50
    assert channel <= channel2


@pytest.fixture()
def vileo_c():
    return Video('AWX4JnAnjBE')


@pytest.fixture()
def plvideo_c():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_video(vileo_c):
    assert str(vileo_c) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert vileo_c.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert vileo_c.id_video == 'AWX4JnAnjBE'


def test_plvideo(plvideo_c):
    assert str(plvideo_c) == 'MoscowPython Meetup 78 - вступление'
    assert plvideo_c.id_play == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    assert plvideo_c.id_video == '4fObz_qw9u4'
    assert plvideo_c.views_video >= '680'


@pytest.fixture()
def playlist_class():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_get_info_for_playlist(playlist_class):
    assert str(playlist_class.total_duration) == '1:49:52'
    assert isinstance(playlist_class.total_duration, datetime.timedelta)
    assert playlist_class.total_duration.total_seconds() == 6592.0


def test_show_best_video(playlist_class):
    assert playlist_class.show_best_video() == "https://youtu.be/cUGyMzWQcGM"


def test_video_id():
    broken_video = Video('broken_video_id')
    assert broken_video.title is None
    assert broken_video.like_count is None

import pytest
from src.channel import Channel
from src.video import Video, PLVideo


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
    assert channel + channel2 == 10256808


def test_lt(channel, channel2):
    assert channel - channel2 == -5409690
    assert channel2 - channel == 5409690


def test_le_lt(channel, channel2):
    assert channel > channel2 == False
    assert channel >= channel2 == False
    assert channel < channel2 == True
    assert channel <= channel2 == True
    assert channel == channel2 == False


@pytest.fixture()
def vileo_c():
    return Video('AWX4JnAnjBE')


@pytest.fixture()
def plvideo_c():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_video(vileo_c):
    assert str(vileo_c) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert vileo_c.name_video == 'GIL в Python: зачем он нужен и как с этим жить'
    assert vileo_c.id_video == 'AWX4JnAnjBE'


def test_plvideo(plvideo_c):
    assert str(plvideo_c) == 'MoscowPython Meetup 78 - вступление'
    assert plvideo_c.id_play == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    assert plvideo_c.id_video == '4fObz_qw9u4'
    assert plvideo_c.views_video >= '680'

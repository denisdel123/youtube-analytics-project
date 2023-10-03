import pytest
from src.channel import Channel


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

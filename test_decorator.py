import pytest
from decorator import name, greeting_decorator, nickname, farewell_decorator

def test_name_decorator():
    actual = name('bob')
    expected = 'Hello there, bob'
    assert actual == expected


def test_nicknname_farewell():
    actual = nickname('Tim')
    expected = 'Well, Tim, It\'s been real. Take care!'
    assert actual == expected
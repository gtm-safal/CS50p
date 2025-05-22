import pytest
from working import convert

def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_3():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
def test_4():
    with pytest.raises(ValueError):
        convert("10 AM to 8:60 PM")
def test_5():
    with pytest.raises(ValueError):
        convert("to ")

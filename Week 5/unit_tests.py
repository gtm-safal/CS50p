
import pytest
from square import square

# def test_square():
    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print(f"Error 2")
    # try:
    #     assert square(4) == 16
    # except AssertionError:
    #     print(f"Error 4")

    # assert square(2) == 4
    # assert square(3) == 9
    # assert square(-2) == 4
    # assert square(-3) == 9
    # assert square(0) == 0

def test_positive():

    assert square(2) == 4
    assert square(3) == 9

def test_negative():

    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# def main():
#     # test_square()


# main()


from numb3rs import validate

def test_correct():
    assert validate("1.2.3.4") == True

def test_wrong():
    assert validate("275.0.0.0") == False



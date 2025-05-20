from bank import value

def test_hello():
    assert value('hello, sir') == 0

def test_h():
    assert value('hey, bro') == 20

def test_HELLO():
    assert value('HELLO, sir') == 0

def test_H():
    assert value('Hey, bro') == 20

def test_others():
    assert value('Namaste, sir') == 100

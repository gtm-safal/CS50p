from jar import Jar

def test_1():
    cookie = Jar()
    assert cookie.cap == 12

def test_2():
    cookie = Jar(14)
    assert cookie.cap == 14

def test_3():
    cookie = Jar()
    cookie.deposit(10)
    assert cookie.cap == 12
    assert cookie.n == 10

def test_4():
    cookie = Jar()
    cookie.deposit(10)
    cookie.withdraw(5)
    assert cookie.cap == 12
    assert cookie.n == 5

from twttr import shorten
import pytest
def main():
    test_shorten()

def test_lower():
    assert shorten('Ball') == 'Bll'
    assert shorten('apple') == 'ppl'

def test_upper():

    assert shorten('ApplE') == 'ppl'
    assert shorten('BASLL') == 'BSLL'

def test_number():

    assert shorten('HELLOO123') == 'HLL123'
    assert shorten('123') == '123'
    assert shorten('a1E2i3o4U5') == '12345'

def test_symbols():

    assert shorten('a(e)i-o+u"a?') == '()-+"?'
    assert shorten('+-*/') == '+-*/'

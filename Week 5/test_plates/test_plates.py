from plates import is_valid

def test_alpha_start():
    assert is_valid('ab22') == True

def test_alpha_check():
    assert is_valid('a12bas') == False
    
def test_len():
    assert is_valid('abcdef') == True

def test_alpha_begin():
    assert is_valid('ab') == True

def test_len1():
    assert is_valid('a') == False

def test_len7():
    assert is_valid('abcderf') == False

def test_num_betwn():
    assert is_valid('aaa22a') == False

def test_num_begin():
    assert is_valid('231aa') == False

def test_num_end():
    assert is_valid('aaa22') == True

def test_zer0_placement():
    assert is_valid('aaa022') == False

def test_alphnum_placement():
    assert is_valid('aa 1') == False



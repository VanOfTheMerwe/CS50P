from plates import is_valid

def test_len():
    assert is_valid("CS05555") == False
    assert is_valid("C") == False
    assert is_valid("CS50") == True

def test_zeropos():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_punt():
    assert is_valid("PB3.10") == False
    assert is_valid("Drik90") == True

def test_alph():
    assert is_valid("AA") == True
    assert is_valid("A33") == False
    assert is_valid("534AAL") == False

def test_num():
    assert is_valid("CA69R") == False
    assert is_valid("2C4T3") == False


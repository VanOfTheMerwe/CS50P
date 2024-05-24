from twttr import shorten

def test_lower(): #testing the lowercase alphanumeric letters.
    assert shorten("man") == "mn"
    assert shorten("Tristin Bellringer") == 'Trstn Bllrngr'
    assert shorten("lukeMelaia") == "lkMl"

def test_upper(): #testing the uppercase alphanumerical letters.
    assert shorten("MAN") == "MN"
    assert shorten("MESSAGE") == "MSSG"

def test_number(): #testing the number.
    assert shorten("24 Hours") == "24 Hrs"

def test_punct(): #testing if the punctuation works.
    assert shorten("I, am him!") == ", m hm!"
    assert shorten("What are you?") == "Wht r y?"


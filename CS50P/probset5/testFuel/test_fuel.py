from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("1/2") == 50
    assert convert("6/10") == 60

def test_errors():
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ZeroDivisionError):
        convert("6/0")


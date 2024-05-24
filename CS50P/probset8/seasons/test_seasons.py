from seasons import date_math
import pytest

def main():
    test_errors



def test_errors():
    with pytest.raises(ValueError):
        date_math('19 January, 1999')
    with pytest.raises(ValueError):
        date_math('cat')
    with pytest.raises(ValueError):
        date_math('2025 09 32')

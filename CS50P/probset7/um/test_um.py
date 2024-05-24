import pytest
from um import count
import sys

def main():
    test_count()
    sys.exit(1)

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

import pytest
from fuel import convert, gauge


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")

def test_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("3/4") == 75 and gauge(75) == "75%"
    
def test_return_empty():
    assert convert("1/100") == 1 and gauge(1) == "E"

def test_return_full():
    assert convert("99/100") == 99 and gauge(99) == "F"


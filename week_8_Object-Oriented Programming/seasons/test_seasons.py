from seasons import validating, get_minutes
from datetime import date


def test_format():
    assert validating("1999-01-01") == ("1999", "01", "01")
    assert validating("February 6th, 1993") == None
    assert validating("1999-3-1") == None

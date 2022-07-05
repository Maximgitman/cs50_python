from twttr import shorten


def test_lower_case():
    assert shorten("hello world!") == "hll wrld!"

def test_upper_case():
    assert shorten("HELLO WORLD!") == "HLL WRLD!"

def test_digits():
    assert shorten("123456789") == "123456789"

def test_punctuation():
    assert shorten(",.!?") == (",.!?")
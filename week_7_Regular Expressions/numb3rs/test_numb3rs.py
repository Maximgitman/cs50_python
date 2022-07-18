from numb3rs import validate


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"0.0.0.0") == True
    assert validate(r"1.1.1.512") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"1.512.1.1") == False
    assert validate(r"512.1.1.1") == False


def test_input_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1") == False
    assert validate(r"cat") == False


from bank import value


def test_zero():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HeLlo") == 0


def test_twenty():
    assert value("hi how are you") == 20
    assert value("Hi David!") == 20
    assert value("HI WORLD!") == 20


def test_hundred():
    assert value("Whats'up") == 100
    assert value("What day is it todat?") == 100

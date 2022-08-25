from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-2)
        jar("8:60 AM to 4:60 PM")
    
    jar2 = Jar(3)
    assert jar2.capacity == 3
    jar3 = Jar(20)
    assert jar3.capacity == 20


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(3)
    assert jar.size == 6


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.deposit(3)
    jar.withdraw(3)
    assert jar.size == 3
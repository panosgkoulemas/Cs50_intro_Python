from jar import Jar
import pytest

def test_init():
    jar = Jar(12,5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar1 = jar = Jar(12,15)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar = Jar(12,5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar = Jar(12,10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(12,12)
    jar.withdraw(10)
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(5)

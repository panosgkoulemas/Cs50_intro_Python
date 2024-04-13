from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(100) == 'F'
    assert gauge(70) == '70%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    with pytest.raises(TypeError):
        gauge('cat')

def test_convert():
    assert convert('1/2') == 50
    assert convert('0/2') == 0
    assert convert('2/2') == 100
    with pytest.raises(ZeroDivisionError):
        convert('2/0')
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert('cat/dog')


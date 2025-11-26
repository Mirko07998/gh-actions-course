import pytest
from calculator import add, subtract, multiply, divide, get_operator_func

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)

def test_get_operator_func():
    assert get_operator_func('+') == add
    assert get_operator_func('-') == subtract
    assert get_operator_func('*') == multiply
    assert get_operator_func('/') == divide
    assert get_operator_func('%') is None
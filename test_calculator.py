import pytest
from calculator import calculate

def test_addition():
    assert calculate(2, '+', 3) == 5

def test_subtraction():
    assert calculate(5, '-', 3) == 2

def test_multiplication():
    assert calculate(2, '*', 3) == 6

def test_division():
    assert calculate(6, '/', 3) == 2

def test_division_by_zero():
    assert calculate(6, '/', 0) is None  # Division by zero should return None

def test_invalid_operator():
    with pytest.raises(KeyError):
        calculate(5, 'invalid_operator', 3)
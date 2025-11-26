import io
import sys
from contextlib import redirect_stdout
from calculator import perform_calculation

def test_addition():
    assert perform_calculation(5, '+', 3) == 8

def test_subtraction():
    assert perform_calculation(5, '-', 3) == 2

def test_multiplication():
    assert perform_calculation(5, '*', 3) == 15

def test_division():
    assert perform_calculation(6, '/', 3) == 2

def test_division_by_zero():
    assert perform_calculation(6, '/', 0) is None

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_division_by_zero()
    print("All tests passed.")
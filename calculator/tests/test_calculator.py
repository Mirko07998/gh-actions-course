import pytest
from calculator.calculator import calculate

def test_addition():
    assert calculate("5", "+", "3") == 8.0

def test_subtraction():
    assert calculate("10", "-", "4") == 6.0

def test_multiplication():
    assert calculate("7", "*", "6") == 42.0

def test_division():
    assert calculate("15", "/", "3") == 5.0

def test_division_by_zero():
    assert calculate("5", "/", "0") == "Error: Cannot divide by zero."

def test_invalid_operator():
    assert calculate("5", "%", "3") == "Error: Unsupported operator."

def test_non_numeric_input():
    assert calculate("five", "+", "three") == "Error: Invalid input. Please enter numeric values."
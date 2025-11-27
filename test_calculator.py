import unittest
from io import StringIO
import sys

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.calculate(1, '+', 1), 2)

    def test_subtraction(self):
        self.assertEqual(calculator.calculate(5, '-', 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculator.calculate(3, '*', 4), 12)

    def test_division(self):
        self.assertEqual(calculator.calculate(10, '/', 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            calculator.calculate(10, '/', 0)
        self.assertEqual(str(context.exception), "Error: Cannot divide by zero.")

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError) as context:
            calculator.calculate(10, '^', 5)
        self.assertEqual(str(context.exception), "Error: Unsupported operator. Please use +, -, *, or /.")

if __name__ == "__main__":
    unittest.main()
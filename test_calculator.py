import io
import sys
import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(5, '+', 3), 8)

    def test_subtraction(self):
        self.assertEqual(calculate(5, '-', 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculate(5, '*', 3), 15)

    def test_division(self):
        self.assertEqual(calculate(6, '/', 3), 2)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, '/', 0)

if __name__ == "__main__":
    unittest.main()
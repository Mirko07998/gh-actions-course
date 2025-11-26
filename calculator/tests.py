import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(2, 3, '+'), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(5, 3, '-'), 2)

    def test_multiplication(self):
        self.assertEqual(calculate(2, 3, '*'), 6)

    def test_division(self):
        self.assertEqual(calculate(6, 3, '/'), 2)

    def test_division_by_zero(self):
        result = calculate(6, 0, '/')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
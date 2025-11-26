import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(2, '+', 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(5, '-', 2), 3)

    def test_multiplication(self):
        self.assertEqual(calculate(4, '*', 2), 8)

    def test_division(self):
        self.assertEqual(calculate(8, '/', 2), 4)

    def test_division_by_zero(self):
        self.assertIsNone(calculate(8, '/', 0))

    def test_invalid_operator(self):
        with self.assertRaises(KeyError):
            calculate(8, '%', 2)  # This case should not be invoked directly
    
if __name__ == '__main__':
    unittest.main()
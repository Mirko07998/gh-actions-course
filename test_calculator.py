import unittest
from calculator import perform_calculation

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(perform_calculation(1, '+', 2), 3)

    def test_subtraction(self):
        self.assertEqual(perform_calculation(5, '-', 2), 3)

    def test_multiplication(self):
        self.assertEqual(perform_calculation(3, '*', 4), 12)

    def test_division(self):
        self.assertEqual(perform_calculation(12, '/', 4), 3)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            perform_calculation(1, '/', 0)
        self.assertEqual(str(context.exception), "Error: Cannot divide by zero.")

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError) as context:
            perform_calculation(1, '%', 2)
        self.assertEqual(str(context.exception), "Error: Unsupported operator.")

if __name__ == '__main__':
    unittest.main()
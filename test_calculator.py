import unittest
from calculator import perform_calculation

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertAlmostEqual(perform_calculation(5, '+', 10), 15)

    def test_subtraction(self):
        self.assertAlmostEqual(perform_calculation(10, '-', 5), 5)

    def test_multiplication(self):
        self.assertAlmostEqual(perform_calculation(3, '*', 7), 21)

    def test_division(self):
        self.assertAlmostEqual(perform_calculation(10, '/', 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            perform_calculation(10, '/', 0)
        self.assertEqual(str(context.exception), "Error: Cannot divide by zero.")

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError) as context:
            perform_calculation(10, '%', 2)
        self.assertEqual(str(context.exception), "Error: Unsupported operator.")

if __name__ == '__main__':
    unittest.main()
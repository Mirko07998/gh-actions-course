import unittest
from calculator import add, subtract, multiply, divide, perform_calculation

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Error: Cannot divide by zero.")

    def test_perform_calculation_addition(self):
        self.assertEqual(perform_calculation(3, '+', 2), 5)

    def test_perform_calculation_subtraction(self):
        self.assertEqual(perform_calculation(5, '-', 2), 3)

    def test_perform_calculation_multiplication(self):
        self.assertEqual(perform_calculation(3, '*', 4), 12)

    def test_perform_calculation_division(self):
        self.assertEqual(perform_calculation(10, '/', 2), 5)

    def test_perform_calculation_invalid_operator(self):
        with self.assertRaises(ValueError) as context:
            perform_calculation(3, '!', 2)
        self.assertEqual(str(context.exception), "Error: Unsupported operator.")

if __name__ == '__main__':
    unittest.main()
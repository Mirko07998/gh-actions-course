import unittest
from calculator import perform_calculation

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(perform_calculation(5, '+', 3), 8)

    def test_subtraction(self):
        self.assertEqual(perform_calculation(5, '-', 3), 2)

    def test_multiplication(self):
        self.assertEqual(perform_calculation(5, '*', 3), 15)

    def test_division(self):
        self.assertEqual(perform_calculation(6, '/', 3), 2)
    
    def test_division_by_zero(self):
        self.assertEqual(perform_calculation(5, '/', 0), "Error: Cannot divide by zero.")

    def test_unsupported_operator(self):
        self.assertEqual(perform_calculation(5, '%', 3), "Error: Unsupported operator.")

    def test_non_numeric_values(self):
        self.assertEqual(perform_calculation("a", '+', 3), "Error: Invalid input.")

if __name__ == '__main__':
    unittest.main()
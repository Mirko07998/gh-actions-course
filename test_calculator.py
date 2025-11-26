import unittest
from calculator import perform_operation

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(perform_operation("3", "+", "5"), 8.0)

    def test_subtraction(self):
        self.assertEqual(perform_operation("10", "-", "4"), 6.0)

    def test_multiplication(self):
        self.assertEqual(perform_operation("2", "*", "3"), 6.0)

    def test_division(self):
        self.assertEqual(perform_operation("9", "/", "3"), 3.0)

    def test_division_by_zero(self):
        self.assertEqual(perform_operation("9", "/", "0"), "Error: Cannot divide by zero.")

    def test_non_numeric_input(self):
        self.assertEqual(perform_operation("abc", "+", "2"), "Error: Please enter valid numeric values.")
    
    def test_unsupported_operator(self):
        self.assertEqual(perform_operation("3", "%", "1"), "Error: Unsupported operator.")

if __name__ == "__main__":
    unittest.main()
import io
import sys
from unittest import TestCase
from unittest.mock import patch
from calculator import add, subtract, multiply, divide

class TestCalculator(TestCase):

    def test_addition(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "Error: Cannot divide by zero.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_function_output(self, mock_stdout):
        input_values = ['10', '+', '5', 'N']
        with patch('builtins.input', side_effect=input_values):
            with self.assertRaises(SystemExit):
                from calculator import main
                main()
        self.assertIn("Result: 15.0", mock_stdout.getvalue())
        self.assertIn("Goodbye!", mock_stdout.getvalue())

if __name__ == '__main__':
    import unittest
    unittest.main()
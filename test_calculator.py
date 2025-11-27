import io
import sys
import unittest
from unittest.mock import patch
from calculator import main

class TestCalculator(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['5', '+', '3'])
    def test_addition(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue().strip().split('\n')[-1]  
            self.assertIn("Result: 8.0", output)
    
    @patch('builtins.input', side_effect=['10', '-', '4'])
    def test_subtraction(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue().strip().split('\n')[-1]  
            self.assertIn("Result: 6.0", output)

    @patch('builtins.input', side_effect=['3', '*', '7'])
    def test_multiplication(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue().strip().split('\n')[-1]  
            self.assertIn("Result: 21.0", output)

    @patch('builtins.input', side_effect=['8', '/', '2'])
    def test_division(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue().strip().split('\n')[-1]  
            self.assertIn("Result: 4.0", output)

    @patch('builtins.input', side_effect=['5', '/', '0'])
    def test_division_by_zero(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue().strip()
            self.assertIn("Error: Cannot divide by zero.", output)

    @patch('builtins.input', side_effect=['five', '+', 'three'])
    def test_non_numeric_input(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main()
            output = fake_stdout.getvalue().strip()
            self.assertIn("Error: Please enter valid numbers.", output)

if __name__ == '__main__':
    unittest.main()
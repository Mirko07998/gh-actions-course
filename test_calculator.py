import io
import sys
import unittest
from calculator import main

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.held_output = io.StringIO()
        sys.stdout = self.held_output
    
    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_addition(self):
        with unittest.mock.patch('builtins.input', side_effect=['10', '+', '5']):
            main()
            self.assertIn("Result: 15.0", self.held_output.getvalue())
    
    def test_subtraction(self):
        with unittest.mock.patch('builtins.input', side_effect=['10', '-', '5']):
            main()
            self.assertIn("Result: 5.0", self.held_output.getvalue())
    
    def test_multiplication(self):
        with unittest.mock.patch('builtins.input', side_effect=['10', '*', '5']):
            main()
            self.assertIn("Result: 50.0", self.held_output.getvalue())
    
    def test_division(self):
        with unittest.mock.patch('builtins.input', side_effect=['10', '/', '2']):
            main()
            self.assertIn("Result: 5.0", self.held_output.getvalue())
    
    def test_division_by_zero(self):
        with unittest.mock.patch('builtins.input', side_effect=['10', '/', '0']):
            main()
            self.assertIn("Error: Cannot divide by zero.", self.held_output.getvalue())
    
    def test_invalid_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['abc', '+', '5']):
            main()
            self.assertIn("Error: Please enter numeric values only.", self.held_output.getvalue())

if __name__ == '__main__':
    unittest.main()
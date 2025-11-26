from django.test import TestCase
from .utils import calculate

class CalculatorTests(TestCase):
    def test_addition(self):
        self.assertEqual(calculate('3', '+', '4'), 7)
    
    def test_subtraction(self):
        self.assertEqual(calculate('10', '-', '4'), 6)
    
    def test_multiplication(self):
        self.assertEqual(calculate('5', '*', '6'), 30)
    
    def test_division(self):
        self.assertAlmostEqual(calculate('8', '/', '2'), 4)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate('5', '/', '0')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate('5', '@', '3')

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate('five', '+', '3')
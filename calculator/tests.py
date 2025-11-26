CONTENT:
from django.test import TestCase

class CalculatorTests(TestCase):
    def test_addition(self):
        response = self.client.post('/', {'num1': '10', 'num2': '5', 'operation': 'add'})
        self.assertContains(response, "Result: 15.0")

    def test_subtraction(self):
        response = self.client.post('/', {'num1': '10', 'num2': '5', 'operation': 'subtract'})
        self.assertContains(response, "Result: 5.0")

    def test_multiplication(self):
        response = self.client.post('/', {'num1': '10', 'num2': '5', 'operation': 'multiply'})
        self.assertContains(response, "Result: 50.0")

    def test_division(self):
        response = self.client.post('/', {'num1': '10', 'num2': '5', 'operation': 'divide'})
        self.assertContains(response, "Result: 2.0")

    def test_division_by_zero(self):
        response = self.client.post('/', {'num1': '10', 'num2': '0', 'operation': 'divide'})
        self.assertContains(response, "Error: Division by zero")

    def test_invalid_input(self):
        response = self.client.post('/', {'num1': 'a', 'num2': '5', 'operation': 'add'})
        self.assertContains(response, "Please enter valid numbers.")
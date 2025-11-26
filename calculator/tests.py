CONTENT:
from django.test import TestCase

class CalculatorTestCase(TestCase):
    def test_addition(self):
        response = self.client.get('/calculate/?num1=10&num2=5&operation=add')
        self.assertEqual(response.json(), {'result': 15})

    def test_subtraction(self):
        response = self.client.get('/calculate/?num1=10&num2=5&operation=subtract')
        self.assertEqual(response.json(), {'result': 5})

    def test_multiplication(self):
        response = self.client.get('/calculate/?num1=10&num2=5&operation=multiply')
        self.assertEqual(response.json(), {'result': 50})

    def test_division(self):
        response = self.client.get('/calculate/?num1=10&num2=5&operation=divide')
        self.assertEqual(response.json(), {'result': 2})

    def test_division_by_zero(self):
        response = self.client.get('/calculate/?num1=10&num2=0&operation=divide')
        self.assertEqual(response.json(), {'error': 'Error: Division by zero'})

    def test_invalid_operation(self):
        response = self.client.get('/calculate/?num1=10&num2=5&operation=invalid')
        self.assertEqual(response.json(), {'error': 'Error: Invalid operation'})

    def test_invalid_input(self):
        response = self.client.get('/calculate/?num1=invalid&num2=5&operation=add')
        self.assertEqual(response.json(), {'error': 'Invalid input'})
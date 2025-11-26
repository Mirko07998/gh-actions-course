```python
from django.test import TestCase
from django.urls import reverse

class CalculatorTests(TestCase):

    def test_addition(self):
        response = self.client.post(reverse('calculate'), {'num1': 1, 'num2': 1, 'operation': 'add'})
        self.assertEqual(response.json()['result'], 2)

    def test_subtraction(self):
        response = self.client.post(reverse('calculate'), {'num1': 10, 'num2': 5, 'operation': 'subtract'})
        self.assertEqual(response.json()['result'], 5)

    def test_multiplication(self):
        response = self.client.post(reverse('calculate'), {'num1': 3, 'num2': 7, 'operation': 'multiply'})
        self.assertEqual(response.json()['result'], 21)

    def test_division(self):
        response = self.client.post(reverse('calculate'), {'num1': 8, 'num2': 2, 'operation': 'divide'})
        self.assertEqual(response.json()['result'], 4)
    
    def test_division_by_zero(self):
        response = self.client.post(reverse('calculate'), {'num1': 8, 'num2': 0, 'operation': 'divide'})
        self.assertEqual(response.json()['result'], 'undefined')

    def test_invalid_operation(self):
        response = self.client.post(reverse('calculate'), {'num1': 8, 'num2': 4, 'operation': 'invalid'})
        self.assertEqual(response.json()['result'], 'Invalid Operation')

    def test_invalid_input(self):
        response = self.client.post(reverse('calculate'), {'num1': 'abc', 'num2': 2, 'operation': 'add'})
        self.assertEqual(response.status_code, 400)
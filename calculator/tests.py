```python
from django.test import TestCase
from django.urls import reverse

class CalculatorTests(TestCase):

    def test_addition(self):
        response = self.client.get(reverse('calculate'), {'num1': 2, 'num2': 3, 'operation': '+'})
        self.assertEqual(response.json()['result'], 5)

    def test_subtraction(self):
        response = self.client.get(reverse('calculate'), {'num1': 5, 'num2': 3, 'operation': '-'})
        self.assertEqual(response.json()['result'], 2)

    def test_multiplication(self):
        response = self.client.get(reverse('calculate'), {'num1': 4, 'num2': 3, 'operation': '*'})
        self.assertEqual(response.json()['result'], 12)

    def test_division(self):
        response = self.client.get(reverse('calculate'), {'num1': 6, 'num2': 2, 'operation': '/'})
        self.assertEqual(response.json()['result'], 3)

    def test_division_by_zero(self):
        response = self.client.get(reverse('calculate'), {'num1': 6, 'num2': 0, 'operation': '/'})
        self.assertEqual(response.status_code, 400)

    def test_invalid_operation(self):
        response = self.client.get(reverse('calculate'), {'num1': 6, 'num2': 2, 'operation': '^'})
        self.assertEqual(response.status_code, 400)

    def test_invalid_input(self):
        response = self.client.get(reverse('calculate'), {'num1': 'a', 'num2': 2, 'operation': '+'})
        self.assertEqual(response.status_code, 400)
```
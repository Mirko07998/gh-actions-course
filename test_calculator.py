import unittest
from calculator import add, subtract, multiply, divide, calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_calculate(self):
        self.assertEqual(calculate(3, '+', 2), 5)
        self.assertEqual(calculate(5, '-', 2), 3)
        self.assertEqual(calculate(4, '*', 2), 8)
        self.assertEqual(calculate(8, '/', 2), 4)
        with self.assertRaises(ValueError):
            calculate(5, '/', 0)
        with self.assertRaises(ValueError):
            calculate(5, '^', 2)

if __name__ == "__main__":
    unittest.main()
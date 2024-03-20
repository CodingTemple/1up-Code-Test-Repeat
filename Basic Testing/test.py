import unittest
from math_functions import divide, factorial

class TestMathFunctions(unittest.TestCase):

    # Testing divide function with normal and edge cases
    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 2), 5)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    # Testing factorial function with normal, edge, and exceptional cases
    def test_factorial_normal(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_non_integer(self):
        with self.assertRaises(ValueError):
            factorial(2.5)

if __name__ == '__main__':
    unittest.main()

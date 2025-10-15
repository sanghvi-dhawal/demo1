# test_sample.py
import unittest

def add(a, b):
    """Simple add function to test."""
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self)::
    self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)

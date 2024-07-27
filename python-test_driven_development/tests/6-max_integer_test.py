#!/usr/bin/python3
"""Unittest for max_integer function.
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_normal_list(self):
        """Test a normal list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_identical_elements(self):
        """Test a list where all elements are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_large_numbers(self):
        """Test a list with very large numbers."""
        self.assertEqual(max_integer([1_000_000, 500_000, 1_500_000]), 1_500_000)

    def test_floats(self):
        """Test a list with floats."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_integers_and_floats(self):
        """Test a list with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_non_integer_elements(self):
        """Test a list with non-integer elements (should raise an error)."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == '__main__':
    unittest.main()

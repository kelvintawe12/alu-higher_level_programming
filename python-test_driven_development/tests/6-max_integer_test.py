#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test a list with multiple integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_another_regular_list(self):
        """Test another list with multiple integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_floats(self):
        """Test a list with floating-point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_int_and_float(self):
        """Test a list with both integers and floating-point numbers"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

if __name__ == '__main__':
    unittest.main()

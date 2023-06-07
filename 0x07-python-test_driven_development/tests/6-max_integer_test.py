#!/usr/bin/python3
"""
    a unittests for the 
    function 
    def max_integer
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_one(self):
        result = max_integer([2, 5, 7, -1, 9, 8])
        self.assertEqual(result, 9)
        return

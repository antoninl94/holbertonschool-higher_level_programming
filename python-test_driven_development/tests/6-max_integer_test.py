#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class testmaxinteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == "__main__":
    unittest.main()

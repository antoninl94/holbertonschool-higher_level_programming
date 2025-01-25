#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class testmaxinteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([-5, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()

import unittest
import random
from Craps import gt_input

class CrapsTests(unittest.TestCase):
    def test_gt_input_invalid_input(self):
        money = "abc"
        expected_result = "Invalid"
        actual_result = gt_input
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
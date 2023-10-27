import unittest
import random
from Craps import gt_input

class CrapsTest(unittest.TestCase):
    def test_gt_input_valid_input(self):
        money = "100"
        expected_result = 100
        actual_result = gt_input()
        self.assertEqual(actual_result, expected_result)

if __name__ =='__main__':
    unittest.main()
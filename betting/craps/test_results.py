import unittest
import random
from Craps import fn_craps

class TestCraps(unittest.TestCase):
    def test_fn_craps_win(self):
        random.seed(1)
        x = 100
        expected_result = 150
        actual_result = fn_craps(x)
        self.assertEqual(actual_result, expected_result)

    def test_fn_craps_lose(self):
        random.seed(2)
        x = 100
        expected_result = 50
        actual_result = fn_craps(x)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
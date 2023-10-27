import unittest
from rockpaperscissors import gt_input

class TestGtInput(unittest.TestCase):
    def test_gt_input_valid_choice(self):
        choice = "R"
        expected_choice = "R"
        actual_choice = gt_input(choice)
        self.assertEqual(actual_choice, expected_choice)

    def test_gt_input_invalid_choice(self):
        choice = "1"
        expected_choice = None
        actual_choice = gt_input(choice)
        self.assertEqual(actual_choice, expected_choice)

if __name__ == '__main__':
    unittest.main()
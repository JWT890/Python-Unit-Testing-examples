import unittest
import random
from Craps import count_games

class TestCraps(unittest.TestCase):
    def test_count_games(self):
        expected_result = "You have won 2 or more games before losing"
        actual_result = count_games()
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
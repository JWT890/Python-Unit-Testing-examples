import unittest
from rockpaperscissors import fn_rps

class TestFnRps(unittest.TestCase):
    def test_fn_rps_tie(self):
        a = "R"
        b = "R"
        expected_result = "Tie"
        actual_result = fn_rps(a, b)
        self.assertEqual(actual_result, expected_result)

    def test_fn_rps_player_a_wins(self):
        a = "R"
        b = "S"
        expected_result = "Player A wins"
        actual_result = fn_rps(a, b)
        self.assertEqual(actual_result, expected_result)

    def test_fn_rps_player_b_wins(self):
        a = "S"
        b = "P"
        expected_result = "Player B wins"
        actual_result = fn_rps(a, b)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
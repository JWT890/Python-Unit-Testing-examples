import unittest
from Roulette import fn_half_board

class TestGame(unittest.TestCase):
    def test_fn_half_board(self):
        self.assertEqual(fn_half_board(10), "Pay 1 to 18")
        self.assertEqual(fn_half_board(20), "Pay 19 to 36")

if __name__ == '__main__':
    unittest.main()
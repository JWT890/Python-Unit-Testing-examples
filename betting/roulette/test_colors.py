import unittest
from Roulette import fn_red_vs_black

class TestGame(unittest.TestCase):
    def test_fn_red_vs_black(self):
        self.assertEqual(fn_red_vs_black(10), "Pay black")
        self.assertEqual(fn_red_vs_black(11), "Pay red")

if __name__ == '__main__':
    unittest.main()
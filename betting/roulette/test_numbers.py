import unittest
from Roulette import fn_single_number, fn_odd_vs_even_number

class TestGame(unittest.TestCase):
    def test_fn_single_number(self):
        self.assertEqual(fn_single_number(10), "Pay the number 10")

    def test_fn_odd_vs_even_number(self):
        self.assertEqual(fn_odd_vs_even_number(10), "Pay even")
        self.assertEqual(fn_odd_vs_even_number(11), "Pay odd")

if __name__ == '__main__':
    unittest.main()
import unittest
from Roulette import fn_game

class TestGame(unittest.TestCase):
    def test_fn_game(self):
        self.assertEqual(fn_game(10), """Pay the number 10
    Pay even
    Pay 1 to 18
    Pay black""")
        
if __name__ == '__main__':
    unittest.main()
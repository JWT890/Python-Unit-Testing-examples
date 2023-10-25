import unittest
from voting import nominee_1, nominee_2

class VotingSystemTest(unittest.TestCase):

    def test_nominee_1_name(self):
        self.assertEqual(nominee_1, "Alice")

    def test_nominee_2_name(self):
        self.assertEqual(nominee_2, "Bob")

if __name__ == '__main__':
    unittest.main()
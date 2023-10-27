import unittest
from racetime import conv_secs_time

class TestConversion(unittest.TestCase):
    def test_conv_secs_time_positive(self):
        self.assertEqual(conv_secs_time(5678), "Final time: 1:34:38")

    def test_conv_secs_time_zero(self):
        self.assertEqual(conv_secs_time(0), "Final time: 0:0:0")

    def test_conv_secs_time_negative(self):
        with self.assertRaises(ValueError):
            conv_secs_time(-1)

if __name__ == '__main__':
    unittest.main()
import unittest
from racetime import run_finish_time

class TestFinishTime(unittest.TestCase):
    def test_run_finish_time_positive(self):
        self.assertEqual(run_finish_time(12, 30), "Finish time in seconds: 28872")

    def test_run_finish_time_zero(self):
        self.assertEqual(run_finish_time(0, 0), "Finish time in seconds: 14622")

    def test_run_finish_time_negative(self):
        with self.assertRaises(ValueError):
            run_finish_time(-1, -1)

if __name__ == '__main__':
    unittest.main()
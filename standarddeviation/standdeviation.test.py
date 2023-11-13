import unittest
from standarddeviation import sd_calc, avg_calc

class TestStandardDeviation(unittest.TestCase):
    def test_sd_calc(self):
        data = [50, 48, 49, 44, 30]
        result = sd_calc(data)
        self.assertAlmostEqual(result, 8.258329128825032)

class TestAverageCalculation(unittest.TestCase):
    def test_avg_calc(self):
        data = [50, 48, 49, 44, 30]
        result = avg_calc(data)
        self.assertEqual(result, 44.2)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
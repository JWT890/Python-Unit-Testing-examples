import unittest

def measurement_conversion(inch, cm):
    print(inch)
    print(cm)

class TestMeasurementConversion(unittest.TestCase):
    def test_convert_zero_inches_to_cm(self):
        inch = 0.0
        cm = 2.54 * inch
        measurement_conversion(inch, cm)
        self.assertEqual(inch, 0.0)
        self.assertEqual(cm, 0.0)

    def test_convert_positive_inches_to_cm(self):
        inch = 1.0
        cm = 2.54 * inch
        measurement_conversion(inch, cm)
        self.assertEqual(inch, 1.0)
        self.assertEqual(cm, 2.54)

    def test_convert_negative_inches_to_cm(self):
        inch = -1.0
        cm = 2.54 * inch
        measurement_conversion(inch, cm)
        self.assertEqual(inch, -1.0)
        self.assertEqual(cm, -2.54)
        

if __name__ == '__main__':
    unittest.main()

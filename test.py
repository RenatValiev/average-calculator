import unittest
from average import average

class TestAverage(unittest.TestCase):
    def test_average_empty_list(self):
        self.assertEqual(average([]), None)

    def test_average_single_value(self):
        self.assertEqual(average([5]), 5)

    def test_average_two_values(self):
        self.assertEqual(average([1, 5]), 3)

    def test_average_negative_values(self):
        self.assertEqual(average([-1, -5]), -3)

    def test_average_float_values(self):
        self.assertAlmostEqual(average([2.5, 3.5]), 3.0, places=1)

if __name__ == '__main__':
    unittest.main()

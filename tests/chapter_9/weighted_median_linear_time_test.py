import unittest
import random
from .weighted_median_test import create_elements
from src.chapter_9.weighted_median_linear_time \
    import weighted_median_linear_time


class TestWeightedMedianLinearTime(unittest.TestCase):
    def test_weighted_median_linear_time(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        weights = [0.1, 0.35, 0.1, 0.05, 0.15, 0.05, 0.2]
        elements = create_elements(values, weights)
        self.assertEqual(3, weighted_median_linear_time(elements).get('value'))

        values = [0.1 for i in range(10)]
        weights = [0.1 for i in range(10)]
        elements = create_elements(values, weights)
        self.assertEqual(
            0.1, weighted_median_linear_time(elements).get('value'))

if __name__ == '__main__':
    unittest.main()
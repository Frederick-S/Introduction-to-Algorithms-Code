import unittest
import random
from src.chapter_9.weighted_median import weighted_median


class TestWeightedMedian(unittest.TestCase):
    def test_weighted_median(self):
        weights = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
        self.assertEqual(0.2, weighted_median(weights))

        weights = [0.1 for i in range(10)]
        self.assertEqual(0.1, weighted_median(weights))

if __name__ == '__main__':
    unittest.main()

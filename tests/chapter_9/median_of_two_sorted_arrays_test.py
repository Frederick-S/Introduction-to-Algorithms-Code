import unittest
import random
from src.chapter_9.median_of_two_sorted_arrays \
    import median_of_two_sorted_arrays


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_median_of_two_sorted_arrays(self):
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 3, 4, 5]
        self.assertEqual(3, median_of_two_sorted_arrays(x, y))

        x = [1, 2, 3, 4, 5]
        y = [6, 7, 8, 9, 10]
        self.assertEqual(5, median_of_two_sorted_arrays(x, y))

        x = [6, 7, 8, 9, 10]
        y = [1, 2, 3, 4, 5]
        self.assertEqual(5, median_of_two_sorted_arrays(x, y))

        x = [i for i in range(1, 101)]
        y = [i for i in range(101, 201)]
        self.assertEqual(100, median_of_two_sorted_arrays(x, y))

        x = [i for i in range(101, 201)]
        y = [i for i in range(1, 101)]
        self.assertEqual(100, median_of_two_sorted_arrays(x, y))

        x = [random.randint(1, 1000) for i in range(1001)]
        x.sort()
        y = [random.randint(1, 1000) for i in range(1001)]
        y.sort()
        z = x + y
        z.sort()
        self.assertEqual(z[999], median_of_two_sorted_arrays(x, y))

if __name__ == '__main__':
    unittest.main()

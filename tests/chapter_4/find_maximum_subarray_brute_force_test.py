import unittest
from sys import maxint
from src.chapter_4.find_maximum_subarray_brute_force import (
    find_maximum_subarray_brute_force
)


class TestMaxiumSubarrayBruteForce(unittest.TestCase):
    def test_maximum_subarray_brute_force(self):
        numbers = []
        self.assertSequenceEqual(
            (-1, -1, -maxint - 1),
            find_maximum_subarray_brute_force(numbers, 0, len(numbers) - 1))

        numbers = [1, 2, 3, 4, 5]
        self.assertSequenceEqual(
            (0, 4, 15),
            find_maximum_subarray_brute_force(numbers, 0, len(numbers) - 1))

        numbers = [-1, -2, -3, -4, -5]
        self.assertSequenceEqual(
            (0, 0, -1),
            find_maximum_subarray_brute_force(numbers, 0, len(numbers) - 1))

        numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertSequenceEqual(
            (3, 6, 6),
            find_maximum_subarray_brute_force(numbers, 0, len(numbers) - 1))

if __name__ == '__main__':
    unittest.main()

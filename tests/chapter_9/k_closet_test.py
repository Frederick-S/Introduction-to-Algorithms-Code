import unittest
import random
from src.chapter_9.k_closet import k_closet


class TestKCloset(unittest.TestCase):
    def test_k_closet(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        closet = k_closet(numbers, 3)
        closet.sort()
        self.assertSequenceEqual([4, 5, 6], closet)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        closet = k_closet(numbers, 3)
        closet.sort()
        self.assertSequenceEqual([4, 5, 6], closet)

        numbers = [1, 2, 4, 8, 16, 32, 64, 128]
        closet = k_closet(numbers, 4)
        closet.sort()
        self.assertSequenceEqual([1, 2, 4, 8], closet)

        numbers = [i for i in range(1, 21)]
        random.shuffle(numbers)
        closet = k_closet(numbers, 10)
        closet.sort()
        self.assertTrue(
            set([i for i in range(6, 16)]) == set(closet) or
            set([i for i in range(5, 15)]) == set(closet))

        numbers = [i for i in range(1, 101)]
        random.shuffle(numbers)
        closet = k_closet(numbers, 30)
        closet.sort()
        self.assertTrue(
            set([i for i in range(36, 66)]) == set(closet) or
            set([i for i in range(35, 65)]) == set(closet))

if __name__ == '__main__':
    unittest.main()

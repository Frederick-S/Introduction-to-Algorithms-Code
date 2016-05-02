import unittest
from src.chapter_6.min_priority_queue import MinPriorityQueue


class TestMinPriorityQueue(unittest.TestCase):
    def test_min_priority_queue(self):
        elements = [1, 2, 6, 0, 4, 7, 8, 12, 5, 9, 13, 15]
        min_priority_queue = MinPriorityQueue(elements)

        self.assertEqual(0, min_priority_queue.minimum())
        self.assertEqual(0, min_priority_queue.extract_min())
        self.assertEqual(1, min_priority_queue.minimum())
        self.assertEqual(11, min_priority_queue.heap_size)

        min_priority_queue.decrease_key(2, 0)
        self.assertEqual(0, min_priority_queue.minimum())

        min_priority_queue.insert(-1)
        self.assertEqual(-1, min_priority_queue.minimum())
        self.assertEqual(12, min_priority_queue.heap_size)

if __name__ == '__main__':
    unittest.main()

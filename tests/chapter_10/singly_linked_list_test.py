import unittest
from src.chapter_10.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def test_singly_linked_list(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert(1)
        singly_linked_list.insert(2)
        singly_linked_list.insert(3)
        self.assertEqual(None, singly_linked_list.search(4))
        self.assertEqual(3, singly_linked_list.search(3).key)

        singly_linked_list.delete(3)
        self.assertEqual(None, singly_linked_list.search(3))

        singly_linked_list.delete(1)
        singly_linked_list.delete(2)
        self.assertTrue(singly_linked_list.is_empty())

if __name__ == '__main__':
    unittest.main()

import unittest
from src.chapter_10.one_pointer_doubly_linked_list \
    import OnePointerDoublyLinkedList


class TestOnePointerDoublyLinkedList(unittest.TestCase):
    def test_one_pointer_doubly_linked_list(self):
        one_pointer_doubly_linked_list = OnePointerDoublyLinkedList()
        one_pointer_doubly_linked_list.insert(1)
        one_pointer_doubly_linked_list.insert(2)
        one_pointer_doubly_linked_list.insert(3)
        self.assertEqual(3, one_pointer_doubly_linked_list.head.key)
        self.assertEqual(2, one_pointer_doubly_linked_list.search(2).key)


if __name__ == '__main__':
    unittest.main()

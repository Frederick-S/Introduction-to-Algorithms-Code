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
        self.assertEqual(1, one_pointer_doubly_linked_list.tail.key)
        self.assertEqual(2, one_pointer_doubly_linked_list.search(2).key)
        self.assertEqual(None, one_pointer_doubly_linked_list.search(4))

        one_pointer_doubly_linked_list.delete(3)
        self.assertEqual(None, one_pointer_doubly_linked_list.search(3))
        self.assertEqual(2, one_pointer_doubly_linked_list.head.key)

        one_pointer_doubly_linked_list.delete(1)
        self.assertEqual(2, one_pointer_doubly_linked_list.tail.key)
        with self.assertRaises(Exception):
            one_pointer_doubly_linked_list.delete(6)


if __name__ == '__main__':
    unittest.main()

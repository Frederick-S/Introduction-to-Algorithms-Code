import unittest
from src.chapter_10.dict_using_singly_linked_list \
    import DictUsingSinglyLinkedList


class TestDictUsingSinglyLinkedList(unittest.TestCase):
    def test_dict_using_singly_linked_list(self):
        dict_using_singly_linked_list = DictUsingSinglyLinkedList()
        dict_using_singly_linked_list.insert(1, 1)
        self.assertEqual(1, dict_using_singly_linked_list.search(1))
        self.assertEqual(None, dict_using_singly_linked_list.search(2))

        dict_using_singly_linked_list.insert(2, 2)
        with self.assertRaises(Exception):
            dict_using_singly_linked_list.insert(2, 2)

        dict_using_singly_linked_list.delete(2)
        with self.assertRaises(Exception):
            dict_using_singly_linked_list.delete(2)


if __name__ == '__main__':
    unittest.main()

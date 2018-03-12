from .singly_linked_list import SinglyLinkedList


class DictUsingSinglyLinkedList(object):
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def insert(self, key, value):
        value = self.search(key)

        if value:
            raise Exception('The specified key already exists')
        else:
            self.singly_linked_list.insert(key, value)

    def delete(self, key):
        value = self.search(key)

        if value:
            self.singly_linked_list.delete(key)
        else:
            raise Exception('The specified key does not exist')

    def search(self, key):
        node = self.singly_linked_list.search(key)

        return node.value if node else None

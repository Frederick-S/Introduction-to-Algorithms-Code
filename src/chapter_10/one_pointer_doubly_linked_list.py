import ctypes


class OnePointerDoublyLinkedNode(object):
    def __init__(self, key):
        self.key = key
        self.np = None


class OnePointerDoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}

    def search(self, key):
        node = self.head
        prev = 0

        while node is not None and node.key != key:
            new_prev = id(node)
            node = ctypes.cast(node.np ^ prev, ctypes.py_object).value
            prev = new_prev

        return node

    def insert(self, key):
        new = OnePointerDoublyLinkedNode(key)

        if self.head is None:
            self.head = new
            self.head.np = 0 ^ 0
        else:
            new.np = id(self.head) ^ 0
            self.head.np = (self.head.np ^ 0) ^ id(new)
            self.head = new

        # Keep reference of each node
        self.nodes[id(new)] = new

    def delete(self, key):
        pass

    def reverse(self, key):
        pass

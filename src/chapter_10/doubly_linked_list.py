class DoublyLinkedNode(object):
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def search(self, key):
        node = self.head

        while node is not None and node.key != key:
            node = node.next

        return node

    def insert(self, key):
        new = DoublyLinkedNode(key)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def delete(self, key):
        current = self.head

        while current is not None and current.key != key:
            current = current.next

        if current is not None:
            if current.prev is not None:
                current.prev.next = current.next
            else:
                self.head = None

            if current.next is not None:
                current.next.prev = current.prev

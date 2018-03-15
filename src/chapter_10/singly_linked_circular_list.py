from .singly_linked_list import SinglyLinkedNode


class SinglyLinkedCircularList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, key, value=None):
        new = SinglyLinkedNode(key, value)

        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head

    def remove_head(self):
        if self.head is not None:
            head, self.head = self.head, self.head.next

            if self.head is None:
                self.tail = None
            else:
                self.tail.next = self.head

            return head

    def search(self, key):
        node = self.head

        while node is not None and node.next != self.head and node.key != key:
            node = node.next

        return node if node is not None and node.key == key else None

    def insert(self, key, value=None):
        new = SinglyLinkedNode(key, value)

        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            new.next, self.head = self.head, new
            self.tail.next = self.head

    def delete(self, key):
        prev = None
        current = self.head

        while current is not None and current.key != key:
            prev = current
            current = current.next

        if current is not None:
            if prev is None:
                self.head = None
                self.tail = None
            else:
                prev.next = current.next

                if prev.next is None:
                    self.tail = prev
                    self.tail.next = self.head

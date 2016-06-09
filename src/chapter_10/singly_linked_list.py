class SinglyLinkedNode(object):
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def remove_head(self):
        if self.head is not None:
            head, self.head = self.head, self.head.next

            return head

    def search(self, key):
        node = self.head

        while node is not None and node.key != key:
            node = node.next

        return node

    def insert(self, key):
        new = SinglyLinkedNode(key)

        if self.head is None:
            self.head = new
        else:
            new.next, self.head = self.head, new

    def delete(self, key):
        prev = None
        current = self.head

        while current is not None and current.key != key:
            prev = current
            current = current.next

        if current is not None:
            if prev is None:
                self.head = None
            else:
                prev.next = current.next

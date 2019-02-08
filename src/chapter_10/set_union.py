from .singly_linked_list import SinglyLinkedList


def set_union(s1, s2):
    new_set = SinglyLinkedList()
    new_set.head = s1.head
    new_set.tail = s1.tail
    new_set.tail.next = s2.head
    new_set.tail = s2.tail

    return new_set

import sys
from .heap_sort import max_heapify, build_max_heap


class PriorityQueue():
    def __init__(self, elements):
        self.elements = elements
        self.heap_size = len(elements)

        build_max_heap(self.elements)

    def insert(self, key):
        self.heap_size += 1
        self.elements.append(-sys.maxsize)
        self.increase_key(self.heap_size - 1, key)

    def maximum(self):
        assert not self.is_empty()

        return self.elements[0]

    def extract_max(self):
        assert not self.is_empty()

        maximum = self.elements[0]
        self.elements[0] = self.elements[self.heap_size - 1]
        self.heap_size -= 1

        max_heapify(self.elements, 0, self.heap_size)

        return maximum

    def increase_key(self, i, key):
        assert i < len(self.elements)
        assert key >= self.elements[i]

        while i > 0 and self.elements[(i - 1) // 2] < key:
            self.elements[i] = self.elements[(i - 1) // 2]
            i = (i - 1) // 2

        self.elements[i] = key

    def is_empty(self):
        return len(self.elements) == 0

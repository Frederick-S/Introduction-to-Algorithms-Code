import sys


class MinPriorityQueue():
    def __init__(self, elements):
        self.elements = elements
        self.heap_size = len(elements)

        self.build_min_heap()

    def insert(self, key):
        self.heap_size += 1
        self.elements.append(sys.maxsize)
        self.decrease_key(self.heap_size - 1, key)

    def minimum(self):
        assert not self.is_empty()

        return self.elements[0]

    def extract_min(self):
        assert not self.is_empty()

        minimum = self.elements[0]
        self.elements[0] = self.elements[self.heap_size - 1]
        self.heap_size -= 1

        self.min_heapify(0)

        return minimum

    def decrease_key(self, i, key):
        assert i < len(self.elements)
        assert key <= self.elements[i]

        while i > 0 and self.elements[(i - 1) // 2] > key:
            self.elements[i] = self.elements[(i - 1) // 2]
            i = (i - 1) // 2

        self.elements[i] = key

    def is_empty(self):
        return len(self.elements) == 0

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minimum = i

        if (left <= self.heap_size - 1 and
                self.elements[left] < self.elements[i]):
            minimum = left

        if (right <= self.heap_size - 1 and
                self.elements[right] < self.elements[minimum]):
            minimum = right

        if minimum != i:
            self.elements[i], self.elements[minimum] = \
                self.elements[minimum], self.elements[i]

            self.min_heapify(minimum)

    def build_min_heap(self):
        for i in range((self.heap_size - 1) // 2, -1, -1):
            self.min_heapify(i)

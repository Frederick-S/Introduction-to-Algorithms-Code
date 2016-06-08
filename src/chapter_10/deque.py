class Deque(object):
    def __init__(self, n):
        self.elements = [-1] * n
        self.size = n
        self.left = -1
        self.right = n

    def is_empty(self):
        return self.left == -1 and self.right == self.size

    def is_full(self):
        return self.right - self.left == 1

    def append(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.right -= 1

        self.elements[self.right] = x

        if self.right == -1:
            self.right == self.size - 1

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')

        x = self.elements[self.right]

        if self.left == self.right:
            self.left = -1
            self.right = self.size
        else:
            self.right += 1

            if self.right == self.size:
                self.right = 0

        return x

    def append_left(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.left += 1

        self.elements[self.left] = x

        if self.left == self.size:
            self.left = 0

    def shift(self):
        if self.is_empty():
            raise Exception('Underflow')

        x = self.elements[self.left]

        if self.left == self.right:
            self.left = -1
            self.right = self.size
        else:
            self.left -= 1

            if self.left == -1:
                self.left = self.size - 1

        return x

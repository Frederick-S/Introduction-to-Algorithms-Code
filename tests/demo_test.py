import unittest
from src import demo

class TestStringMethods(unittest.TestCase):
    def test_sum(self):
        self.assertTrue(5, demo.sum(1, 4))


if __name__ == '__main__':
    unittest.main()
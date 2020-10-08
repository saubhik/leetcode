import unittest

from binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def test_example_1(self):
        assert Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4

    def test_example_2(self):
        assert Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1

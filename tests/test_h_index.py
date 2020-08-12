import unittest

from h_index import Solution


class TestHIndex(unittest.TestCase):
    def test_example_1(self):
        assert Solution().hIndex(citations=[3, 0, 6, 1, 5]) == 3

    def test_example_2(self):
        assert Solution().hIndex(citations=[]) == 0

import unittest

from champagne_tower import Solution


class TestChampagneTower(unittest.TestCase):
    def test_example_1(self):
        assert Solution().champagneTower(poured=1, query_row=1, query_glass=1) == 0.0

    def test_example_2(self):
        assert Solution().champagneTower(poured=2, query_row=1, query_glass=1) == 0.5

    def test_example_3(self):
        assert (
            Solution().champagneTower(poured=100000009, query_row=33, query_glass=17)
            == 1.0
        )

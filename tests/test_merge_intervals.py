from unittest import TestCase

from merge_intervals import Solution


class TestMergeIntervals(TestCase):
    def test_example_1(self):
        assert Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [
            [1, 6],
            [8, 10],
            [15, 18],
        ]

    def test_example_2(self):
        assert Solution().merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]

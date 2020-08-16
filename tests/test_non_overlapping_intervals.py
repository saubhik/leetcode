import unittest

from non_overlapping_intervals import Solution


class TestNonOverlappingIntervals(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]])
            == 1
        )

    def test_example_2(self):
        assert Solution().eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2

    def test_example_3(self):
        assert Solution().eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]) == 0

    def test_example_4(self):
        assert (
            Solution().eraseOverlapIntervals(
                intervals=[[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]
            )
            == 4
        )

    def test_example_5(self):
        assert Solution().eraseOverlapIntervals(intervals=[]) == 0

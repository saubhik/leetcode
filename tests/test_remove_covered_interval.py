import unittest

from remove_covered_interval import Solution


class TestRemoveCoveredInterval(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]) == 2
        )

    def test_example_2(self):
        assert Solution().removeCoveredIntervals(intervals=[[1, 4], [2, 3]]) == 1

    def test_example_3(self):
        assert Solution().removeCoveredIntervals(intervals=[[0, 10], [5, 12]]) == 2

    def test_example_4(self):
        assert (
            Solution().removeCoveredIntervals(intervals=[[3, 10], [4, 10], [5, 11]])
            == 2
        )

    def test_example_5(self):
        assert (
            Solution().removeCoveredIntervals(intervals=[[1, 2], [1, 4], [3, 4]]) == 1
        )

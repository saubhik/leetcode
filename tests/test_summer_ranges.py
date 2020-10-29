import unittest

from summary_ranges import Solution


class TestSummaryRanges(unittest.TestCase):
    def test_example_1(self):
        assert Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7]) == [
            "0->2",
            "4->5",
            "7",
        ]

    def test_example_2(self):
        assert Solution().summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]) == [
            "0",
            "2->4",
            "6",
            "8->9",
        ]

    def test_example_3(self):
        assert Solution().summaryRanges(nums=[]) == []

    def test_example_4(self):
        assert Solution().summaryRanges(nums=[0]) == ["0"]

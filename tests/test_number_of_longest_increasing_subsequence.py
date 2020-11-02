import unittest

from number_of_longest_increasing_subsequence import Solution, SolutionSegmentTree


class TestNumberOfLongestIncreasingSubsequence(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findNumberOfLIS(nums=[1, 3, 5, 4, 7]) == 2
        assert SolutionSegmentTree().findNumberOfLIS(nums=[1, 3, 5, 4, 7]) == 2

    def test_example_2(self):
        assert Solution().findNumberOfLIS(nums=[2, 2, 2, 2, 2]) == 5
        assert SolutionSegmentTree().findNumberOfLIS(nums=[2, 2, 2, 2, 2]) == 5

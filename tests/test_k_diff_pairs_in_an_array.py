import unittest

from k_diff_pairs_in_an_array import Solution, OfficialSolution


class TestKDiffPairsInAnArray(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findPairs(nums=[3, 1, 4, 1, 5], k=2) == 2
        assert OfficialSolution().findPairs(nums=[3, 1, 4, 1, 5], k=2) == 2

    def test_example_2(self):
        assert Solution().findPairs(nums=[1, 2, 3, 4, 5], k=1) == 4
        assert OfficialSolution().findPairs(nums=[1, 2, 3, 4, 5], k=1) == 4

    def test_example_3(self):
        assert Solution().findPairs(nums=[1, 3, 1, 5, 4], k=0) == 1
        assert OfficialSolution().findPairs(nums=[1, 3, 1, 5, 4], k=0) == 1

    def test_example_4(self):
        assert Solution().findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3) == 2
        assert (
            OfficialSolution().findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3) == 2
        )

    def test_example_5(self):
        assert Solution().findPairs(nums=[-1, -2, -3], k=1) == 2
        assert OfficialSolution().findPairs(nums=[-1, -2, -3], k=1) == 2

    def test_example_6(self):
        assert Solution().findPairs(nums=[1, 1, 1, 1, 1], k=0) == 1
        assert OfficialSolution().findPairs(nums=[1, 1, 1, 1, 1], k=0) == 1

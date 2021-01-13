import unittest

from combination_sum import OfficialSolution, Solution


class TestCombinationSum(unittest.TestCase):
    def test_example_1(self):
        assert Solution().combinationSum(candidates=[2, 3, 6, 7], target=7) == [
            [2, 2, 3],
            [7],
        ]
        assert OfficialSolution().combinationSum(candidates=[2, 3, 6, 7], target=7) == [
            [2, 2, 3],
            [7],
        ]

    def test_example_2(self):
        assert Solution().combinationSum(candidates=[2, 3, 5], target=8) == [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5],
        ]
        assert OfficialSolution().combinationSum(candidates=[2, 3, 5], target=8) == [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5],
        ]

    def test_example_3(self):
        assert Solution().combinationSum(candidates=[2], target=1) == []
        assert OfficialSolution().combinationSum(candidates=[2], target=1) == []

    def test_example_4(self):
        assert Solution().combinationSum(candidates=[1], target=1) == [[1]]
        assert OfficialSolution().combinationSum(candidates=[1], target=1) == [[1]]

    def test_example_5(self):
        assert Solution().combinationSum(candidates=[1], target=2) == [[1, 1]]
        assert OfficialSolution().combinationSum(candidates=[1], target=2) == [[1, 1]]

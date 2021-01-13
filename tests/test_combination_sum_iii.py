import unittest

from combination_sum_iii import Solution, SolutionFour, SolutionThree, SolutionTwo


class TestCombinationSumIII(unittest.TestCase):
    def test_example_1(self):
        assert Solution().combinationSum3(k=3, n=7) == [[1, 2, 4]]
        assert SolutionTwo().combinationSum3(k=3, n=7) == [[1, 2, 4]]
        assert SolutionThree().combinationSum3(k=3, n=7) == [[1, 2, 4]]
        assert SolutionFour().combinationSum3(k=3, n=7) == [[1, 2, 4]]

    def test_example_2(self):
        assert Solution().combinationSum3(k=3, n=9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        assert SolutionTwo().combinationSum3(k=3, n=9) == [
            [2, 3, 4],
            [1, 3, 5],
            [1, 2, 6],
        ]
        assert SolutionThree().combinationSum3(k=3, n=9) == [
            [1, 2, 6],
            [1, 3, 5],
            [2, 3, 4],
        ]
        assert SolutionFour().combinationSum3(k=3, n=9) == [
            [1, 2, 6],
            [1, 3, 5],
            [2, 3, 4],
        ]

    def test_example_3(self):
        assert Solution().combinationSum3(k=2, n=18) == []
        assert SolutionTwo().combinationSum3(k=2, n=18) == []
        assert SolutionThree().combinationSum3(k=2, n=18) == []
        assert SolutionFour().combinationSum3(k=2, n=18) == []

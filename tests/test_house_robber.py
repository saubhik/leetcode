import unittest

from house_robber import Solution, SolutionTwo


class TestHouseRobber(unittest.TestCase):
    def test_example_1(self):
        assert Solution().rob(nums=[1, 2, 3, 1]) == 4
        assert SolutionTwo().rob(nums=[1, 2, 3, 1]) == 4

    def test_example_2(self):
        assert Solution().rob(nums=[2, 7, 9, 3, 1]) == 12
        assert SolutionTwo().rob(nums=[2, 7, 9, 3, 1]) == 12

    def test_example_3(self):
        assert Solution().rob(nums=[2, 1, 1, 2]) == 4
        assert SolutionTwo().rob(nums=[2, 1, 1, 2]) == 4

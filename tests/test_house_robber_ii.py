import unittest

from house_robber_ii import Solution


class TestHouseRobberII(unittest.TestCase):
    def test_example_1(self):
        assert Solution().rob(nums=[2, 3, 2]) == 3

    def test_example_2(self):
        assert Solution().rob(nums=[1, 2, 3, 1]) == 4

    def test_example_3(self):
        assert Solution().rob(nums=[0]) == 0

    def test_example_4(self):
        assert Solution().rob(nums=[98, 3, 3, 2, 1, 99]) == 104

    def test_example_5(self):
        assert Solution().rob(nums=[200, 3, 140, 20, 10]) == 340

    def test_example_6(self):
        assert Solution().rob(nums=[1, 1, 1, 2]) == 3

    def test_example_7(self):
        assert Solution().rob(nums=[1]) == 1

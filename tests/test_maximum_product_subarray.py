import unittest

from maximum_product_subarray import Solution, SolutionTwo


class TestMaximumProductSubarray(unittest.TestCase):
    def test_example_1(self):
        assert Solution().maxProduct(nums=[2, 3, -2, 4]) == 6
        assert SolutionTwo().maxProduct(nums=[2, 3, -2, 4]) == 6

    def test_example_2(self):
        assert Solution().maxProduct(nums=[-2, 0, -1]) == 0
        assert SolutionTwo().maxProduct(nums=[-2, 0, -1]) == 0

    def test_example_3(self):
        assert Solution().maxProduct(nums=[-2]) == -2
        assert SolutionTwo().maxProduct(nums=[-2]) == -2

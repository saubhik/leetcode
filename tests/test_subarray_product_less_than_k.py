import unittest

from subarray_product_less_than_k import Solution, OfficialSolution


class TestSubarrayProductLessThanK(unittest.TestCase):
    def test_example_1(self):
        assert Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100) == 8
        assert (
            OfficialSolution().numSubarrayProductLessThanKApproach2(
                nums=[10, 5, 2, 6], k=100
            )
            == 8
        )

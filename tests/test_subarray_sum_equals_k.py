import unittest

from subarray_sum_equals_k import Solution


class TestSubarraySumEqualsK(unittest.TestCase):
    def test_example(self):
        assert Solution().subarraySum(nums=[1, 1, 1], k=2) == 2

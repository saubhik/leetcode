from typing import List
from unittest import TestCase


class Solution:
    """
    Linear Scan of Array.
    Time Complexity: O(n).
    Space Complexity: O(1).
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        for num in arr:
            if num - last > k:
                return last + k
            k -= num - last - 1
            last = num
        return last + k


class TestFindKthPositive(TestCase):
    def test_example_1(self):
        assert Solution().findKthPositive(arr=[2, 3, 4, 7, 11], k=5) == 9

    def test_example_2(self):
        assert Solution().findKthPositive(arr=[1, 2, 3, 4], k=2) == 6

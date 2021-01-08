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


class SolutionTwo:
    """
    Binary Search.
    Time Complexity: O(logn).
    Space Complexity: O(1).
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        lo, hi = 0, n - 1
        while lo < hi - 1:
            mid = hi - (hi - lo) // 2
            # Number of missing elements before arr[mid] = arr[mid] - mid - 1
            missing = arr[mid] - (mid + 1)
            if missing >= k:
                hi = mid
            else:
                lo = mid

        # Now we have an interval [lo,lo+1]
        missing_left = arr[lo] - (lo + 1)
        missing_right = arr[hi] - (hi + 1)

        if missing_left >= k:
            # On left of interval.
            return k
        elif missing_right < k:
            # On right of interval.
            return arr[hi] + k - missing_right
        else:
            # In the interval.
            return arr[lo] + k - missing_left


class TestFindKthPositive(TestCase):
    def test_example_1(self):
        assert Solution().findKthPositive(arr=[2, 3, 4, 7, 11], k=5) == 9
        assert SolutionTwo().findKthPositive(arr=[2, 3, 4, 7, 11], k=5) == 9

    def test_example_2(self):
        assert Solution().findKthPositive(arr=[1, 2, 3, 4], k=2) == 6
        assert SolutionTwo().findKthPositive(arr=[1, 2, 3, 4], k=2) == 6

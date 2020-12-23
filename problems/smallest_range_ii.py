from typing import List
from unittest import TestCase


class Solution:
    """
    Sort A.

    First observation:
    For any solution B for which p is the greatest index for which B[p]=A[p]+K, we can
    have a solution B' with B'[i]=A[i]+K for all i<=p.
    The maximum cannot go up since B[p]=B'[p]. Others are less than B[p]=B'[p].
    The minimum cannot go down, since everything was bumped up for i<=p.

    Consider each index as such a p.
    The maximum candidates are A[p]+K and A[right]-K.
    The minimum candidates are A[0]+K and A[p+1]-K.
    Track the minimum difference.

    Time Complexity: O(nlgn)
    Space Complexity: O(n) due to Python's Timsort sort() call.
    """

    def smallestRangeII(self, A: List[int], K: int) -> int:
        n, ans = len(A), float("inf")
        A.sort()
        for i in range(n):
            max_cand = max(A[i] + K, A[n - 1] - K)
            min_cand = A[0] + K if i == n - 1 else min(A[0] + K, A[i + 1] - K)
            ans = min(ans, max_cand - min_cand)
        return ans


class TestSmallestRangeII(TestCase):
    def test_example_1(self):
        assert Solution().smallestRangeII(A=[1], K=0) == 0

    def test_example_2(self):
        assert Solution().smallestRangeII(A=[0, 10], K=2) == 6

    def test_example_3(self):
        assert Solution().smallestRangeII(A=[1, 3, 6], K=3) == 3

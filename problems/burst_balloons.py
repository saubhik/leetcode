from collections import defaultdict
from typing import List
from unittest import TestCase


class Solution:
    """
    Dynamic Programming With Divide & Conquer:
    dp(left, right): max coins for the open interval (left, right).

    Adding the ith balloon:
    dp(left, i) + (nums[left] * nums[i] * nums[right]) + dp(i, right)

    Example:
    3, 1, 5, 8
    dp(-1, 4) = max(
        dp(-1, 0) + 1 * 3 * 1 + dp(0, 4),
        dp(-1, 1) + 1 * 1 * 1 + dp(1, 4),
        dp(-1, 2) + 1 * 5 * 1 + dp(2, 4),
        dp(-1, 3) + 1 * 8 * 1 + dp(3, 4)
    )

    Time Complexity: O(n^2 * n) = O(n^3).
        Each dp[i][j] takes O(n) time.
        There are O(n^2) dp[i][j].
        So, in total O(n^3).
    Space Complexity: O(n^2).
    """

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(defaultdict)

        def _helper(left: int, right: int):
            # Memoize
            if left in dp and right in dp[left]:
                return dp[left][right]

            ans = 0
            for i in range(left + 1, right):
                nums_left = nums[left] if left >= 0 else 1
                nums_right = nums[right] if right < n else 1
                ans = max(
                    ans,
                    _helper(left=left, right=i)
                    + nums_left * nums[i] * nums_right
                    + _helper(left=i, right=right),
                )

            dp[left][right] = ans
            return ans

        return _helper(left=-1, right=n)


class SolutionTwo:
    """
    Dynamic Programming with Bottom-Up Approach
    This is tabulation.

    Time Complexity: O(n^2 * n) = O(n^3).
    Space Complexity: O(n^2).
    """

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = max(
                    dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                    for k in range(i + 1, j)
                )
        return dp[0][n - 1]


class TestSolution(TestCase):
    def test_example_1(self):
        assert Solution().maxCoins(nums=[3, 1, 5, 8]) == 167
        assert SolutionTwo().maxCoins(nums=[3, 1, 5, 8]) == 167

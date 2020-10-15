from typing import List


class Solution:
    """
    Straight Forward DP.
    [1,98,3,4,99,6]
    dp[i] = Maximum amount robbed till house i, including i.
    dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i])
    Consider the maximum of the dp[i]s for the answer.

    Or, we can consider:
    dp[i] = Maximum amount robbed till house i (might or might not include i)
    dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    For this problem:
    Either consider houses from 1 to n-1 or consider houses from 0 to n-2,
    where n = len(nums).

    Minor extension of original House Robber problem.

    Time Complexity: O(n).
    Space Complexity: O(1).
    """

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # Solve the DP for houses from [0, n-1).
        pre = current_start0 = 0
        for i in range(n - 1):
            pre, current_start0 = current_start0, max(current_start0, nums[i] + pre)

        # Solve the DP for houses from [1, n).
        pre = current_start1 = 0
        for i in range(1, n):
            pre, current_start1 = current_start1, max(current_start1, nums[i] + pre)

        return max(current_start0, current_start1)

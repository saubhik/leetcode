from collections import defaultdict
from typing import List


class Solution:
    # Find if there is a subset with a given sum.
    # Memoization based DP solution.
    # Time Complexity:
    #   - O(2**n) without memoization.
    #   - O(sum(nums) * len(nums)) = O(mn), since that's what we store in cache.
    # Space Complexity:
    #   - O(mn) for the cache, O(n) for the recursion call stack.
    #   - O(mn) overall.
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums, len_nums = sum(nums), len(nums)

        # If odd, cannot have 2 subsets with equal sum.
        if sum_nums % 2:
            return False

        subset_sum = sum_nums // 2

        # For memoization.
        cache = defaultdict(defaultdict)

        # Check if there is a subset whose sum equals subset_sum.
        # For every element, we can either consider it or not consider it.
        def _has_subset(index: int, subset_sum: int) -> bool:
            if index in cache and subset_sum in cache[index]:
                return cache[index][subset_sum]

            if subset_sum == 0:
                return True

            if index == len_nums or subset_sum < 0:
                return False

            cache[index][subset_sum] = _has_subset(
                index=index + 1, subset_sum=subset_sum - nums[index]
            ) or _has_subset(index=index + 1, subset_sum=subset_sum)

            return cache[index][subset_sum]

        return _has_subset(index=0, subset_sum=subset_sum)


class SolutionTwo:
    # Tabulation or Bottom-Up DP.
    # Time Complexity:
    #   - O(mn)
    # Space Complexity:
    #   - O(m)
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums, len_nums = sum(nums), len(nums)

        if sum_nums % 2:
            return False

        subset_sum = sum_nums // 2

        dp = [False] * (subset_sum + 1)

        dp[0] = True

        # dp[i][j] means whether there is a subset in nums[0...i]
        # having a sum of j.
        # So, dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        # Since, we only consider i-1 when solving the sub-problem for i,
        # we can have 1D DP array.
        for i in range(len_nums):
            # Observe how we decrement the j to make sure dp[j-nums[i]]
            # comes from previous iteration.
            for j in range(subset_sum, 0, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]

        return dp[subset_sum]

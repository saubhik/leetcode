from typing import List


class Solution:
    # Gets TLEd.
    # Brute Force
    # Time: O(n^2)
    # Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                ans = max(ans, prod)
        return ans


class SolutionTwo:
    # Time: O(n)
    # Space: O(1)
    #
    # Two DP variables.
    # One for storing the max ending at i.
    # Another for storing the min ending at i.
    # Because of negative numbers, min at i-1 might become max at i.
    # And vice-versa.
    # Calculation of dp_max_i requires dp_min_(i-1) and dp_max_(i-1).
    # Calculation of dp_min_i requires dp_min_(i-1) and dp_max_(i-1).
    # Return the maximum value of dp_max_i encountered so far.
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        dp_max_i = dp_min_i = 1
        for num in nums:
            dp_max_i, dp_min_i = (
                max(dp_max_i * num, dp_min_i * num, num),
                min(dp_max_i * num, dp_min_i * num, num),
            )
            ans = max(ans, dp_max_i)
        return ans

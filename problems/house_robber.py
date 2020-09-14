from typing import List


class Solution:
    # Dynamic Programming Take 1
    #
    # Time: O(n)
    # Space: O(1)
    #
    # The sub problem at index i is:
    # What is the maximum amount that I can rob if we consider only the numbers from
    # index 0 to index i.
    #
    # It is the maximum of:
    # 1. maximum amount that I can rob if I consider numbers from index 0 to
    #    index i-1. Call it prev_max.
    # 2. maximum amount that I can rob if I consider numbers from index 0 to
    #    index i-2 + the number at index i. Call it curr_max.
    def rob(self, nums: List[int]) -> int:
        curr_max = prev_max = 0
        for num in nums:
            curr_max, prev_max = max(prev_max + num, curr_max), curr_max
        return curr_max


class SolutionTwo:
    # Dynamic Programming Take 2
    #
    # Time: O(n)
    # Space: O(1)
    #
    # I often tend to think of DP sub problem as: What is the answer to the
    # optimization objective for some intermediate index i, and including the index i.
    #
    # Note that difference above is that we might not include index i.
    #
    # Then the answer to the global optimization problem is the maximum of the
    # optimized answers to these sub problems as we iterate over all possible index i.
    #
    # Maximum amount I can rob including house at index i is the maximum of:
    # 1. Maximum amount I can rob including house at index i-2 + nums[i].
    # 2. Maximum amount I can rob including house at index i-3 + nums[i].
    #
    # So, we need to keep 3 DP state variables.
    # Call them:
    # ls = last sum
    # lls = second last sum
    # llls = third last sum
    def rob(self, nums: List[int]) -> int:
        ls = lls = llls = ans = 0
        for i in range(len(nums)):
            ls, lls, llls = max(lls + nums[i], llls + nums[i]), ls, lls
            ans = max(ans, ls)
        return ans

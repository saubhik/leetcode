from typing import List


class Solution:
    # Gets TLEd.
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                if prod < k:
                    ans += 1
                else:
                    break

        return ans


class OfficialSolution:
    def numSubarrayProductLessThanKApproach2(self, nums: List[int], k: int) -> int:
        """
        == Approach #2: Sliding Window ==
        == Intuition ==
        For each right, call opt(right) the smallest left so that the product of the
        subarray nums[left] * nums[left+1] * ... * nums[right] is less than k. opt is a
        monotone increasing function, so we can use a sliding window.

        == Algorithm ==
        Our loop invariant is that left is the smallest value so that the product in the
        window prod = nums[left] * nums[left+1] * ... * nums[right] is less than k.
        For every right, we update left and prod to maintain this invariant. Then, the
        number of intervals with subarray product less than k and with right-most
        coordinate right, is right - left + 1. We'll count all of these for each value
        of right.

        == Complexity Analysis ==
        - Time Complexity: O(N), where N is the length of nums. At each iteration, we
            either increase left or right, and we both left and right can be incremented
            at most N times.
        - Space Complexity: O(1).
        """
        left = right = 0
        prod = 1
        ans = 0

        while right < len(nums):
            # Case 1. Include right.
            if prod * nums[right] < k:
                prod *= nums[right]
                ans += right - left + 1
                right += 1
            # Case 2. Cannot include right.
            # Case 2a. If left and right point to same element.
            elif left == right:
                left += 1
                right += 1
            # Case 2b. Left points to a left element.
            else:
                prod //= nums[left]
                left += 1

        return ans

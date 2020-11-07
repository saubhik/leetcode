from math import ceil
from typing import List


class Solution:
    # Binary Search.
    # Time Complexity: O(nlg(max(nums))).
    # Space Complexity: O(1).
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def _eval(d):
            result = 0
            for num in nums:
                result += ceil(num / d)
            return result

        left, right = 1, max(nums)

        if _eval(left) <= threshold:
            return left

        while right - left > 1:
            # If left=1, right=2, then mid=2
            mid = right - (right - left) // 2
            if _eval(mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1

        # right might not be <= threshold.
        if _eval(right) > threshold:
            return right + 1

        # Now right <= threshold
        # left might not be <= threshold
        if _eval(left) > threshold:
            return right

        # Now left <= threshold.
        return left

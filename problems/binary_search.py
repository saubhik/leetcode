from typing import List


class Solution:
    # Time Complexity: O(lgN)
    # Space Complexity: O(1)
    # This is same as official solution.
    # (If you do not want to include right in consideration, then be
    # consistent, and keep right always the one to not be included in
    # consideration.)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            # 1, 2, 5, 7, 9
            # 0, 1, 2, 3, 4
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1

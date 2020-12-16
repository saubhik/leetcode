from typing import List
from unittest import TestCase


class Solution:
    # Similar to Merge operation in MergeSort.
    # Time Complexity: O(n) time.
    # Space Complexity: O(n) if considering output.
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n, index = len(nums), None
        for i in range(n):
            if nums[i] < 0:
                index = i
            nums[i] *= nums[i]

        if index is None:
            return nums

        # Merge nums[index...0] & nums[index+1...n-1]
        ans = []
        i, j = index, index + 1
        while i >= 0 and j < n:
            if nums[i] <= nums[j]:
                ans.append(nums[i])
                i -= 1
            else:
                # nums[i] > nums[j]
                ans.append(nums[j])
                j += 1

        while i >= 0:
            ans.append(nums[i])
            i -= 1

        while j < n:
            ans.append(nums[j])
            j += 1

        return ans


class TestSolution(TestCase):
    def test_example_1(self):
        assert Solution().sortedSquares(nums=[-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

    def test_example_2(self):
        assert Solution().sortedSquares(nums=[-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

    def test_example_3(self):
        assert Solution().sortedSquares(nums=[-5, -4, -3, -2, -1]) == [1, 4, 9, 16, 25]

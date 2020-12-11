from typing import List
from unittest import TestCase


class Solution:
    # Time Complexity: O(n^2).
    # Space Complexity: O(1).
    def removeDuplicates(self, nums: List[int]) -> int:
        i, n = 1, len(nums)
        while i < n:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        return n


class SolutionTwo:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, n = 0, 0, len(nums)
        for j in range(n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


class TestRemoveDuplicates(TestCase):
    def test_example_1(self):
        assert Solution().removeDuplicates(nums=[1, 1, 2]) == 2
        assert SolutionTwo().removeDuplicates(nums=[1, 1, 2]) == 2

    def test_example_2(self):
        assert Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
        assert SolutionTwo().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

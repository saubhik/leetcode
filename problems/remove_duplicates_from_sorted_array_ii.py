from typing import List
from unittest import TestCase


class Solution:
    # Two Pointers.
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 0, 1
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                count += 1
            else:
                count = 1

            if count <= 2:
                i += 1
                nums[i] = nums[j]

        return i + 1


class TestRemoveDuplicates(TestCase):
    def test_example_1(self):
        # 1, 1, 2, 2, 3
        assert Solution().removeDuplicates(nums=[1, 1, 1, 2, 2, 3]) == 5

    def test_example_2(self):
        # 0, 0, 1, 1, 2, 3, 3
        assert Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7

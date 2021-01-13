from typing import List
from unittest import TestCase


class Solution:
    # Merge operation of Merge Sort using pointers initialized to the end of
    # both lists.
    # Time Complexity: O(m+n).
    # Space Complexity: O(1).
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1

        while m and n:
            # Undecided
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[pos] = nums1[m - 1]
                nums1[m - 1] = 0
                m -= 1
            else:
                nums1[pos] = nums2[n - 1]
                n -= 1
            pos -= 1

        while n:
            nums1[pos] = nums2[n - 1]
            n -= 1
            pos -= 1


class TestMerge(TestCase):
    def test_example_1(self):
        nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
        Solution().merge(nums1=nums1, m=3, nums2=nums2, n=3)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_example_2(self):
        nums1, nums2 = [1], []
        Solution().merge(nums1=nums1, m=1, nums2=nums2, n=0)
        assert nums1 == [1]

from typing import List
from unittest import TestCase


class Solution:
    # Linear Scan using hashmap.
    # Time Complexity: O(n).
    # Space Complexity: O(n) due to hashmap.
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hashmap, i = {p[0]: p for p in pieces}, 0
        while i < len(arr):
            if not arr[i] in hashmap:
                return False
            j, piece = 0, hashmap[arr[i]]
            while j < len(piece):
                if piece[j] != arr[i]:
                    return False
                i, j = i + 1, j + 1
        return True


class TestCanFormArray(TestCase):
    def test_example_1(self):
        assert Solution().canFormArray(arr=[85], pieces=[[85]]) is True

    def test_example_2(self):
        assert Solution().canFormArray(arr=[15, 88], pieces=[[88], [15]]) is True

    def test_example_3(self):
        assert Solution().canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]]) is False

    def test_example_4(self):
        assert (
            Solution().canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]])
            is True
        )

    def test_example_5(self):
        assert Solution().canFormArray(arr=[1, 3, 5, 7], pieces=[[2, 4, 6, 8]]) is False

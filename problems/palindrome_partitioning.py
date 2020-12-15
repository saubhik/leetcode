from typing import List
from unittest import TestCase


class Solution:
    # Straight Forward Backtracking.
    # Time Complexity: O(n * 2^n).
    # Space Complexity: O(n^2) additional space.
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans, palindrome = [], [[False] * n for _ in range(n)]

        def backtrack(pos: int, curr: List[str]):
            if pos == n:
                nonlocal ans
                ans.append(list(curr))

            for i in range(pos, n):
                left, right = pos, i
                if s[left] == s[right] and (
                    right - left <= 2 or palindrome[left + 1][right - 1]
                ):
                    palindrome[left][right] = True
                    curr.append(s[left : right + 1])  # O(n) time.
                    backtrack(pos=i + 1, curr=curr)
                    curr.pop()

        backtrack(pos=0, curr=[])

        return ans


class TestSolution(TestCase):
    def test_example_1(self):
        assert Solution().partition(s="aab") == [["a", "a", "b"], ["aa", "b"]]

    def test_example_2(self):
        assert Solution().partition(s="a") == [["a"]]

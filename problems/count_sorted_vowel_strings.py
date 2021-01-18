from unittest import TestCase


class Solution:
    # Backtracking with Memoization.
    # Time Complexity: O(n).
    # Space Complexity: O(n).
    def countVowelStrings(self, n: int) -> int:
        dp = [[-1] * 5 for _ in range(n)]

        def backtrack(curr_len: int, next_char: int):
            if curr_len == n:
                return 1

            if dp[curr_len][next_char] != -1:
                return dp[curr_len][next_char]

            count = 0
            for i in range(next_char, 5):
                count += backtrack(curr_len=curr_len + 1, next_char=i)

            dp[curr_len][next_char] = count
            return count

        return backtrack(curr_len=0, next_char=0)


class SolutionTwo:
    # Solution to Diophantine Equation: x1 + x2 + x3 + x4 + x5 = n.
    # Time Complexity: O(1).
    # Space Complexity: O(1).
    def countVowelStrings(self, n: int) -> int:
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24


class TestCountVowelStrings(TestCase):
    def test_example_1(self):
        assert Solution().countVowelStrings(n=1) == 5
        assert SolutionTwo().countVowelStrings(n=1) == 5

    def test_example_2(self):
        assert Solution().countVowelStrings(n=2) == 15
        assert SolutionTwo().countVowelStrings(n=2) == 15

    def test_example_3(self):
        assert Solution().countVowelStrings(n=33) == 66045
        assert SolutionTwo().countVowelStrings(n=33) == 66045

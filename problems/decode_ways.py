from typing import Optional, Dict
from unittest import TestCase


class Solution:
    """
    Recursion (Dynamic Programming) with Memoization.
    Time Complexity: O(n), where n is length of s.
    Space Complexity: O(n), where n is length of s.
    """

    def numDecodings(self, s: str, cache: Optional[Dict] = None) -> int:
        if cache is None:
            cache = {}

        if s in cache:
            return cache[s]

        if not s:
            return 1

        if s[0] == "0":
            return 0

        ans = self.numDecodings(s=s[1:], cache=cache)
        if 10 <= int(s[:2]) <= 26:  # Must have len == 2.
            ans += self.numDecodings(s=s[2:], cache=cache)

        cache[s] = ans
        return ans


class SolutionTwo:
    """
    Iterative DP (Tabulation).
    In the above, cache[s] is the number of ways to decode substring s.
    cache["123"]=cache["23"]+cache["3"]
    This is our inspiration for the dp table.

    Time Complexity: O(n).
    Space Complexity: O(1).
    """

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp1 = 0  # Represents dp[i].
        dp2 = 1 if s[-1] != "0" else 0  # Represents dp[i+1].
        dp3 = 1  # Represents dp[i+2].
        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                dp1 = 0
            else:
                dp1 = dp2
                if 10 <= int(s[i : i + 2]) <= 26:
                    dp1 += dp3
            dp2, dp3 = dp1, dp2
        return dp1 if n > 1 else dp2


class TestNumDecodings(TestCase):
    def test_example_1(self):
        """
        numDecodings(s="12")
            =numDecodings(s="2")+numDecodings(s="")
            =1+1
            =2
        """
        assert Solution().numDecodings(s="12") == 2
        assert SolutionTwo().numDecodings(s="12") == 2

    def test_example_2(self):
        """
        numDecodings(s="226")
            =numDecodings(s="26")+numDecodings(s="6")
            =2+1
            =3
        """
        assert Solution().numDecodings(s="226") == 3
        assert SolutionTwo().numDecodings(s="226") == 3

    def test_example_3(self):
        assert Solution().numDecodings(s="0") == 0
        assert SolutionTwo().numDecodings(s="0") == 0

    def test_example_4(self):
        assert Solution().numDecodings(s="1") == 1
        assert SolutionTwo().numDecodings(s="1") == 1

    def test_example_5(self):
        assert Solution().numDecodings(s="10") == 1
        assert SolutionTwo().numDecodings(s="10") == 1

from collections import Counter


class Solution:
    # Time: O(N)
    # Space: O(1), since alphabet size is fixed.
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = Counter(s)
        for count in counter.values():
            ans += count - 1 if count % 2 else count
        return ans if ans == len(s) else ans + 1

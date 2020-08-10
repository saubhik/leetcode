class Solution:
    # Time: O(n)
    # Space: O(1)
    def titleToNumber(self, s: str) -> int:
        result = 0
        for ch in s:
            result = 26 * result + ord(ch) - ord("A") + 1
        return result

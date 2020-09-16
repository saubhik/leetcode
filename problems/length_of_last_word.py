class Solution:
    # Time: O(n)
    # Space: O(1)
    def lengthOfLastWord(self, s: str) -> int:
        curr_len = last_len = 0
        for char in s:
            if char == " " and curr_len > 0:
                last_len, curr_len = curr_len, 0
            elif char != " ":
                curr_len += 1

        if curr_len > 0:
            last_len = curr_len

        return last_len

class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def maxPower(self, s: str) -> int:
        last, count, max_count = "", 1, 0
        for char in s:
            if char == last:
                count += 1
            else:
                last, count = char, 1
            max_count = max(count, max_count)
        return max_count

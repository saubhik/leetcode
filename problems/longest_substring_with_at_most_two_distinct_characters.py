from collections import defaultdict


class Solution:
    # Sliding Window.
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_length = 0
        left = right = 0
        chars = defaultdict(int)  # Mapping from char to right most index.
        while right < len(s):
            # Expansion.
            if len(chars) < 2 or s[right] in chars:
                chars[s[right]] = right
                right += 1

            else:
                # len(chars) == 2
                # Shrink
                while chars[s[left]] != left:
                    left += 1

                chars.pop(s[left])
                left += 1

            max_length = max(max_length, right - left)

        return max_length

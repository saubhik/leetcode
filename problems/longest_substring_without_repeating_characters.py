from unittest import TestCase


class Solution:
    """
    Greedy with linear scan using hashmap.
    Time Complexity: O(n).
    Space Complexity: O(n).

    Maintain a Hashmap: character->index.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, hashmap, ans = 0, {}, 0
        for pos in range(len(s)):
            if s[pos] in hashmap and hashmap[s[pos]] >= start:
                start = hashmap[s[pos]] + 1
            hashmap[s[pos]] = pos
            ans = max(ans, pos - start + 1)
        return ans


class TestLengthOfLongestSubstring(TestCase):
    def test_example_1(self):
        assert Solution().lengthOfLongestSubstring(s="abcabcbb") == 3

    def test_example_2(self):
        assert Solution().lengthOfLongestSubstring(s="bbbbb") == 1

    def test_example_3(self):
        assert Solution().lengthOfLongestSubstring(s="pwwkew") == 3

    def test_example_4(self):
        assert Solution().lengthOfLongestSubstring(s="") == 0

    def test_example_5(self):
        assert Solution().lengthOfLongestSubstring(s="abba") == 2

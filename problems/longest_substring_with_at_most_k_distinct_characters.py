from collections import OrderedDict
from unittest import TestCase


class Solution:
    # We need to have O(n) solution given the constraints.
    # s = "eceba"
    # We would like to get as much of the repeating characters as possible.
    # This is similar to Longest Substring with At Most 2 Distinct Characters.
    # Sliding window with two pointers initialised at same position?
    # left=0, right=0
    # Increment right if number of distinct characters <= k.
    # Maintain a hashmap of character counts in window.
    # Increment left if number of distinct characters > k.
    #
    # Sliding Window.
    # Time Complexity: O(n)
    # Space Complexity: O(1) additional space.
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = right = 0
        ans = 0
        counter = {}
        while right < len(s):
            if len(counter) <= k:
                counter[s[right]] = counter.get(s[right], 0) + 1
                if len(counter) <= k:
                    ans = max(ans, right - left + 1)
                right += 1
            else:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1

        return ans


class SolutionTwo:
    # Sliding Window using Ordered Dict of rightmost indices.
    # Time Complexity: O(n)
    # Space Complexity: O(1) additional space.
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0

        if not s or not k:
            return ans

        left = right = 0
        rightmost_index = OrderedDict()

        while right < len(s):
            if s[right] in rightmost_index:
                del rightmost_index[s[right]]

            rightmost_index[s[right]] = right

            if len(rightmost_index) <= k:
                right += 1
            else:
                left = rightmost_index.popitem(last=False)[1] + 1

            ans = max(ans, right - left)

        return ans


class TestLengthOfLongestSubstringKDistinct(TestCase):
    def test_example_1(self):
        assert Solution().lengthOfLongestSubstringKDistinct(s="eceba", k=2) == 3
        assert SolutionTwo().lengthOfLongestSubstringKDistinct(s="eceba", k=2) == 3

    def test_example_2(self):
        assert Solution().lengthOfLongestSubstringKDistinct(s="aa", k=1) == 2
        assert SolutionTwo().lengthOfLongestSubstringKDistinct(s="aa", k=1) == 2

    def test_example_3(self):
        assert Solution().lengthOfLongestSubstringKDistinct(s="a", k=2) == 1
        assert SolutionTwo().lengthOfLongestSubstringKDistinct(s="a", k=2) == 1

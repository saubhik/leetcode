from unittest import TestCase


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        parity = 0
        for char in s:
            parity ^= 1 << ord(char)
        return parity & (parity - 1) == 0


class TestCanPermutePalindrome(TestCase):
    def test_example_1(self):
        assert Solution().canPermutePalindrome(s="code") is False

    def test_example_2(self):
        assert Solution().canPermutePalindrome(s="aab") is True

    def test_example_3(self):
        assert Solution().canPermutePalindrome(s="carerac") is True

import unittest

from longest_palindrome import Solution


class TestLongestPalindrome(unittest.TestCase):
    def test_example(self):
        assert Solution().longestPalindrome(s="abccccdd") == 7
        assert Solution().longestPalindrome(s="ccc") == 3

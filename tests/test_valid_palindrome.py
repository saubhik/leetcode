import unittest

from valid_palindrome import Solution, SolutionTwo


class TestValidPalindrome(unittest.TestCase):
    def test_example(self):
        assert Solution().isPalindrome(s="A man, a plan, a canal: Panama") is True
        assert Solution().isPalindrome(s="race a car") is False
        assert Solution().isPalindrome(s="") is True
        assert Solution().isPalindrome(s="0P") is False

    def test_example_two(self):
        assert SolutionTwo().isPalindrome(s="A man, a plan, a canal: Panama") is True
        assert SolutionTwo().isPalindrome(s="race a car") is False
        assert SolutionTwo().isPalindrome(s="") is True
        assert SolutionTwo().isPalindrome(s="0P") is False

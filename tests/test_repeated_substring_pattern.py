import unittest

from repeated_substring_pattern import SolutionRabinKarp


class TestRepeatedSubstringPattern(unittest.TestCase):
    def test_example_1(self):
        assert SolutionRabinKarp().repeatedSubstringPattern(s="abab") is True

    def test_example_2(self):
        assert SolutionRabinKarp().repeatedSubstringPattern(s="aba") is False

    def test_example_3(self):
        assert SolutionRabinKarp().repeatedSubstringPattern(s="abcabcabc") is True

    def test_example_4(self):
        assert SolutionRabinKarp().repeatedSubstringPattern(s="aa") is True

    def test_example_5(self):
        assert SolutionRabinKarp().repeatedSubstringPattern(s="aaa") is True

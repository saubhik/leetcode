from unittest import TestCase

from longest_substring_with_at_most_two_distinct_characters import Solution


class TestLongestSubstringWithAtMostTwoDistinctCharacters(TestCase):
    def test_example_1(self):
        assert Solution().lengthOfLongestSubstringTwoDistinct(s="eceba") == 3

    def test_example_2(self):
        assert Solution().lengthOfLongestSubstringTwoDistinct(s="ccaabbb") == 5

    def test_example_3(self):
        assert Solution().lengthOfLongestSubstringTwoDistinct(s="") == 0

    def test_example_4(self):
        assert Solution().lengthOfLongestSubstringTwoDistinct(s="a") == 1

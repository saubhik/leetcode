import unittest

from word_break import OfficialSolution


class TestWordBreak(unittest.TestCase):
    def test_example_1(self):
        assert (
            OfficialSolution().wordBreakApproach1(
                s="leetcode", wordDict=["leet", "code"]
            )
            is True
        )
        assert (
            OfficialSolution().wordBreakApproach2(
                s="leetcode", wordDict=["leet", "code"]
            )
            is True
        )

    def test_example_2(self):
        assert (
            OfficialSolution().wordBreakApproach1(
                s="applepenapple", wordDict=["apple", "pen"]
            )
            is True
        )
        assert (
            OfficialSolution().wordBreakApproach2(
                s="applepenapple", wordDict=["apple", "pen"]
            )
            is True
        )

    def test_example_3(self):
        assert (
            OfficialSolution().wordBreakApproach1(
                s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
            )
            is False
        )
        assert (
            OfficialSolution().wordBreakApproach2(
                s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
            )
            is False
        )

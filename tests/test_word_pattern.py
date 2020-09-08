import unittest

from word_pattern import Solution, SolutionTwo


class TestWordPattern(unittest.TestCase):
    def test_example_1(self):
        assert Solution().wordPattern(pattern="abba", str="dog cat cat dog") is True
        assert SolutionTwo().wordPattern(pattern="abba", str="dog cat cat dog") is True

    def test_example_2(self):
        assert Solution().wordPattern(pattern="abba", str="dog cat cat fish") is False
        assert (
            SolutionTwo().wordPattern(pattern="abba", str="dog cat cat fish") is False
        )

    def test_example_3(self):
        assert Solution().wordPattern(pattern="aaaa", str="dog cat cat dog") is False
        assert SolutionTwo().wordPattern(pattern="aaaa", str="dog cat cat dog") is False

    def test_example_4(self):
        assert Solution().wordPattern(pattern="abba", str="dog dog dog dog") is False
        assert SolutionTwo().wordPattern(pattern="abba", str="dog dog dog dog") is False

    def test_example_5(self):
        assert Solution().wordPattern(pattern="aaa", str="aa aa aa aa") is False
        assert SolutionTwo().wordPattern(pattern="aaa", str="aa aa aa aa") is False

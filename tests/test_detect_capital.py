import unittest

from detect_capital import Solution, SolutionTwo


class TestDetectCapital(unittest.TestCase):
    def setUp(self) -> None:
        self.solve = Solution().detectCapitalUse
        self.solveTwo = SolutionTwo().detectCapitalUse

    def test_examples(self):
        assert self.solve(word="USA") is True
        assert self.solve(word="FlaG") is False
        assert self.solve(word="") is True
        assert self.solve(word="heLLo") is False

    def test_examples_two(self):
        assert self.solveTwo(word="USA") is True
        assert self.solveTwo(word="FlaG") is False
        assert self.solveTwo(word="") is True
        assert self.solveTwo(word="heLLo") is False

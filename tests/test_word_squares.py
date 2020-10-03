import unittest

from word_squares import OfficialSolution


class TestWordSquares(unittest.TestCase):
    def test_example_1(self):
        assert OfficialSolution().wordSquares(
            words=["area", "lead", "wall", "lady", "ball"]
        ) == [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]]
        assert OfficialSolution().wordSquaresApproach1(
            words=["area", "lead", "wall", "lady", "ball"]
        ) == [["wall", "area", "lead", "lady"], ["ball", "area", "lead", "lady"]]

    def test_example_2(self):
        assert OfficialSolution().wordSquares(
            words=["abat", "baba", "atan", "atal"]
        ) == [["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]]
        assert OfficialSolution().wordSquaresApproach1(
            words=["abat", "baba", "atan", "atal"]
        ) == [["baba", "abat", "baba", "atan"], ["baba", "abat", "baba", "atal"]]

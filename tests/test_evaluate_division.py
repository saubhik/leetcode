import unittest

from evaluate_division import OfficialSolution


class TestEvaluateDivision(unittest.TestCase):
    def test_example_1(self):
        assert OfficialSolution().calcEquation(
            equations=[["a", "b"], ["b", "c"]],
            values=[2.0, 3.0],
            queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        ) == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    def test_example_2(self):
        assert OfficialSolution().calcEquation(
            equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
            values=[1.5, 2.5, 5.0],
            queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        ) == [3.75000, 0.40000, 5.00000, 0.20000]

    def test_example_3(self):
        assert OfficialSolution().calcEquation(
            equations=[["a", "b"]],
            values=[0.5],
            queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
        ) == [0.50000, 2.00000, -1.00000, -1.00000]

    def test_example_4(self):
        assert OfficialSolution().calcEquation(
            equations=[["a", "e"], ["b", "e"]],
            values=[4.0, 3.0],
            queries=[["a", "b"], ["e", "e"], ["x", "x"]],
        ) == [1.3333333333333333, 1.00000, -1.00000]

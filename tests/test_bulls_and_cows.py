import unittest

from bulls_and_cows import Solution, SolutionTwo


class TestBullsAndCows(unittest.TestCase):
    def test_example_1(self):
        assert Solution().getHint(secret="1807", guess="7810") == "1A3B"
        assert SolutionTwo().getHint(secret="1807", guess="7810") == "1A3B"

    def test_example_2(self):
        assert Solution().getHint(secret="1123", guess="0111") == "1A1B"
        assert SolutionTwo().getHint(secret="1123", guess="0111") == "1A1B"

    def test_example_3(self):
        assert Solution().getHint(secret="1122", guess="1222") == "3A0B"
        assert SolutionTwo().getHint(secret="1122", guess="1222") == "3A0B"

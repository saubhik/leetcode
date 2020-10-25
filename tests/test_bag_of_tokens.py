import unittest

from bag_of_tokens import Solution


class TestBagOfTokens(unittest.TestCase):
    def test_example_1(self):
        assert Solution().bagOfTokensScore(tokens=[100], P=50) == 0

    def test_example_2(self):
        assert Solution().bagOfTokensScore(tokens=[100, 200], P=150) == 1

    def test_example_3(self):
        assert Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], P=200) == 2

    def test_example_4(self):
        assert Solution().bagOfTokensScore(tokens=[], P=200) == 0

    def test_example_5(self):
        assert Solution().bagOfTokensScore(tokens=[26], P=51) == 1

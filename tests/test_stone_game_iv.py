import unittest

from stone_game_iv import Solution


class TestStoneGameIV(unittest.TestCase):
    def test_example_1(self):
        assert Solution().winnerSquareGame(n=1) is True
        assert Solution().winnerSquareGameDP(n=1) is True

    def test_example_2(self):
        assert Solution().winnerSquareGame(n=2) is False
        assert Solution().winnerSquareGameDP(n=2) is False

    def test_example_3(self):
        assert Solution().winnerSquareGame(n=4) is True
        assert Solution().winnerSquareGameDP(n=4) is True

    def test_example_4(self):
        assert Solution().winnerSquareGame(n=7) is False
        assert Solution().winnerSquareGameDP(n=7) is False

    def test_example_5(self):
        assert Solution().winnerSquareGame(n=17) is False
        assert Solution().winnerSquareGameDP(n=17) is False

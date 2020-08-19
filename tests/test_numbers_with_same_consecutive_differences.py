import unittest

from numbers_with_same_consecutive_differences import Solution


class TestNumbersWithSameConsecutiveDifference(unittest.TestCase):
    def test_example_1(self):
        assert Solution().numsSameConsecDiff(N=3, K=7) == [181, 292, 707, 818, 929]

    def test_example_2(self):
        assert set(Solution().numsSameConsecDiff(N=2, K=1)) == {
            10,
            12,
            21,
            23,
            32,
            34,
            43,
            45,
            54,
            56,
            65,
            67,
            76,
            78,
            87,
            89,
            98,
        }

    def test_example_3(self):
        assert Solution().numsSameConsecDiff(N=1, K=0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_example_4(self):
        assert Solution().numsSameConsecDiff(N=1, K=1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_example_5(self):
        assert Solution().numsSameConsecDiff(N=2, K=0) == [
            11,
            22,
            33,
            44,
            55,
            66,
            77,
            88,
            99,
        ]

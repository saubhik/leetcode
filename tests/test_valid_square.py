from unittest import TestCase

from valid_square import Solution


class TestValidSquare(TestCase):
    def test_example_1(self):
        assert (
            Solution().validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]) is True
        )

    def test_example_2(self):
        assert (
            Solution().validSquare(p1=[1, 0], p2=[-1, 0], p3=[0, 1], p4=[0, -1]) is True
        )

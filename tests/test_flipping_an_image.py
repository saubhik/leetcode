from unittest import TestCase

from problems.filpping_an_image import Solution


class TestFlippingAnImage(TestCase):
    def test_example_1(self):
        assert Solution().flipAndInvertImage(A=[[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [
            [1, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
        ]

    def test_example_2(self):
        assert Solution().flipAndInvertImage(
            A=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        ) == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

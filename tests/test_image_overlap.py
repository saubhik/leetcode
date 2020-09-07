import unittest

from image_overlap import Solution


class TestImageOverlap(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().largestOverlap(
                A=[[1, 1, 0], [0, 1, 0], [0, 1, 0]], B=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]
            )
            == 3
        )

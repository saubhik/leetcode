import unittest

from maximum_distance_in_arrays import Solution


class TestMaximumDistanceInArrays(unittest.TestCase):
    def test_example_1(self):
        assert Solution().maxDistance(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]) == 4

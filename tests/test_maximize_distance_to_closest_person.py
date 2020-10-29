import unittest

from maximize_distance_to_closest_person import Solution


class TestMaximizeDistanceToClosestPerson(unittest.TestCase):
    def test_example_1(self):
        assert Solution().maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1]) == 2

    def test_example_2(self):
        assert Solution().maxDistToClosest(seats=[1, 0, 0, 0]) == 3

    def test_example_3(self):
        assert Solution().maxDistToClosest(seats=[0, 1]) == 1

    def test_example_4(self):
        assert Solution().maxDistToClosest(seats=[0, 0, 1]) == 2

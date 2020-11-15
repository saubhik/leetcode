from unittest import TestCase

from poor_pigs import Solution


class TestPoorPigs(TestCase):
    def test_example_1(self):
        assert Solution().poorPigs(buckets=8, minutesToDie=1, minutesToTest=1) == 3

    def test_example_2(self):
        assert Solution().poorPigs(buckets=1000, minutesToTest=60, minutesToDie=15) == 5

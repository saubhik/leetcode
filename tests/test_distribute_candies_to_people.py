import unittest

from distribute_candies_to_people import Solution


class TestDistributeCandiesToPeople(unittest.TestCase):
    def test_example_1(self):
        assert Solution().distributeCandies(candies=7, num_people=4) == [1, 2, 3, 1]

    def test_example_2(self):
        assert Solution().distributeCandies(candies=10, num_people=3) == [5, 2, 3]

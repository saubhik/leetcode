import unittest

from asteroid_collision import Solution


class TestAsteroidCollision(unittest.TestCase):
    def test_example_1(self):
        assert Solution().asteroidCollision(asteroids=[5, 10, -5]) == [5, 10]

    def test_example_2(self):
        assert Solution().asteroidCollision(asteroids=[8, -8]) == []

    def test_example_3(self):
        assert Solution().asteroidCollision(asteroids=[10, 2, -5]) == [10]

    def test_example_4(self):
        assert Solution().asteroidCollision(asteroids=[-2, -1, 1, 2]) == [-2, -1, 1, 2]

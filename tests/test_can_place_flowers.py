from unittest import TestCase

from can_place_flowers import Solution


class TestCanPlaceFlowers(TestCase):
    def test_example_1(self):
        assert Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1) is True

    def test_example_2(self):
        assert Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2) is False

    def test_example_3(self):
        assert Solution().canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2) is False

    def test_example_4(self):
        assert Solution().canPlaceFlowers(flowerbed=[1, 0, 1, 0, 1, 0, 1], n=0) is True

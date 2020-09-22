import unittest

from car_pooling import Solution


class TestCarPooling(unittest.TestCase):
    def test_example_1(self):
        assert Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4) is False

    def test_example_2(self):
        assert Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5) is True

    def test_example_3(self):
        assert Solution().carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3) is True

    def test_example_4(self):
        assert (
            Solution().carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11)
            is True
        )

from unittest import TestCase

from sliding_window_maximum import Solution


class TestSlidingWindowMaximum(TestCase):
    def test_example_1(self):
        assert Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [
            3,
            3,
            5,
            5,
            6,
            7,
        ]

    def test_example_2(self):
        assert Solution().maxSlidingWindow(nums=[1], k=1) == [1]

    def test_example_3(self):
        assert Solution().maxSlidingWindow(nums=[1, -1], k=1) == [1, -1]

    def test_example_4(self):
        assert Solution().maxSlidingWindow(nums=[9, 11], k=2) == [11]

    def test_example_5(self):
        assert Solution().maxSlidingWindow(nums=[4, -2], k=2) == [4]

    def test_example_6(self):
        assert Solution().maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3) == [3, 3, 2, 5]

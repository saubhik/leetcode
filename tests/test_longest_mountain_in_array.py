from unittest import TestCase

from longest_mountain_in_array import Solution


class TestLongestMountainInArray(TestCase):
    def test_example_1(self):
        assert Solution().longestMountain(A=[2, 1, 4, 7, 3, 2, 5]) == 5

    def test_example_2(self):
        assert Solution().longestMountain(A=[2, 2, 2]) == 0

    def test_example_3(self):
        assert Solution().longestMountain(A=[0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 11

    def test_example_4(self):
        assert Solution().longestMountain(A=[2, 3]) == 0

    def test_example_5(self):
        assert Solution().longestMountain(A=[0, 1, 0]) == 3

    def test_example_6(self):
        assert Solution().longestMountain(A=[2, 0, 2, 0]) == 3

    def test_example_7(self):
        assert Solution().longestMountain(A=[2, 3, 3, 2, 0, 2]) == 0

    def test_example_8(self):
        assert Solution().longestMountain(A=[875, 884, 239, 731, 723, 685]) == 4

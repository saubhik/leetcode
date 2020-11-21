from unittest import TestCase

from search_in_rotated_sorted_array_ii import Solution


class TestSearchInRotatedSortedArrayII(TestCase):
    def test_example_1(self):
        assert Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0) is True

    def test_example_2(self):
        assert Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=3) is False

    def test_example_3(self):
        assert Solution().search(nums=[1], target=1) is True

    def test_example_4(self):
        assert Solution().search(nums=[1, 3, 1, 1], target=3) is True

    def test_example_5(self):
        assert Solution().search(nums=[1, 1, 3], target=3) is True

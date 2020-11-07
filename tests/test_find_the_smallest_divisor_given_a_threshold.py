from unittest import TestCase

from find_the_smallest_divisor_given_a_threshold import Solution


class TestFindTheSmallestDivisorGivenAThreshold(TestCase):
    def test_example_1(self):
        assert Solution().smallestDivisor(nums=[1, 2, 5, 9], threshold=6) == 5

    def test_example_2(self):
        assert Solution().smallestDivisor(nums=[2, 3, 5, 7, 11], threshold=11) == 3

    def test_example_3(self):
        assert Solution().smallestDivisor(nums=[19], threshold=5) == 4

    def test_example_4(self):
        assert (
            Solution().smallestDivisor(
                nums=[962551, 933661, 905225, 923035, 990560], threshold=10
            )
            == 495280
        )

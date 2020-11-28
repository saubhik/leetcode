from unittest import TestCase

from partition_equal_subset_sum import Solution, SolutionTwo


class TestPartitionEqualSubsetSum(TestCase):
    def test_example_1(self):
        assert Solution().canPartition(nums=[1, 5, 11, 5]) is True
        assert SolutionTwo().canPartition(nums=[1, 5, 11, 5]) is True

    def test_example_2(self):
        assert Solution().canPartition(nums=[1, 2, 3, 5]) is False
        assert SolutionTwo().canPartition(nums=[1, 2, 3, 5]) is False

    def test_example_3(self):
        assert Solution().canPartition(nums=[1, 2, 5]) is False
        assert SolutionTwo().canPartition(nums=[1, 2, 5]) is False

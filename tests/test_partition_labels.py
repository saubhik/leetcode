import unittest

from partition_labels import Solution, SolutionTwo


class TestPartitionLabels(unittest.TestCase):
    def test_example_1(self):
        assert Solution().partitionLabels(S="ababcbacadefegdehijhklij") == [9, 7, 8]
        assert SolutionTwo().partitionLabels(S="ababcbacadefegdehijhklij") == [9, 7, 8]

    def test_example_2(self):
        assert Solution().partitionLabels(S="") == []
        assert SolutionTwo().partitionLabels(S="") == []

    def test_example_3(self):
        assert Solution().partitionLabels(S="abcdefghijklmnopqrstuvwxyz") == [1] * 26
        assert SolutionTwo().partitionLabels(S="abcdefghijklmnopqrstuvwxyz") == [1] * 26

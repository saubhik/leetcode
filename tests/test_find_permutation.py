import unittest

from find_permutation import Solution


class TestFindPermutation(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findPermutation(s="I") == [1, 2]

    def test_example_2(self):
        assert Solution().findPermutation(s="DI") == [2, 1, 3]

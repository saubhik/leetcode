import unittest

from maximum_xor_of_two_numbers_in_an_array import Solution


class TestMaximumXOROfTwoNumbersInAnArray(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findMaximumXOR(nums=[3, 10, 5, 25, 2, 8]) == 28

    def test_example_2(self):
        assert Solution().findMaximumXOR(nums=[3, 10, 5]) == 15

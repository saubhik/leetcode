import unittest

from consecutive_characters import Solution


class TestConsecutiveCharacters(unittest.TestCase):
    def test_example_1(self):
        assert Solution().maxPower(s="leetcode") == 2

    def test_example_2(self):
        assert Solution().maxPower(s="abbcccddddeeeeedcba") == 5

    def test_example_3(self):
        assert Solution().maxPower(s="triplepillooooow") == 5

    def test_example_4(self):
        assert Solution().maxPower(s="hooraaaaaaaaaaay") == 11

    def test_example_5(self):
        assert Solution().maxPower(s="tourist") == 1

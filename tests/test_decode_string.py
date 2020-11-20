from unittest import TestCase

from decode_string import Solution


class TestDecodeString(TestCase):
    def test_example_1(self):
        assert Solution().decodeString(s="3[a]2[bc]") == "aaabcbc"

    def test_example_2(self):
        assert Solution().decodeString(s="3[a2[c]]") == "accaccacc"

    def test_example_3(self):
        assert Solution().decodeString(s="2[abc]3[cd]ef") == "abcabccdcdcdef"

    def test_example_4(self):
        assert Solution().decodeString(s="abc3[cd]xyz") == "abccdcdcdxyz"

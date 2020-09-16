import unittest

from length_of_last_word import Solution


class TestLengthOfLastWord(unittest.TestCase):
    def test_example_1(self):
        assert Solution().lengthOfLastWord(s="Hello World") == 5

    def test_example_2(self):
        assert Solution().lengthOfLastWord(s=" Hello   World    ") == 5

    def test_example_3(self):
        assert Solution().lengthOfLastWord(s="   ") == 0

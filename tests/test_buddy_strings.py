import unittest

from buddy_strings import Solution


class TestBuddyStrings(unittest.TestCase):
    def test_example_1(self):
        assert Solution().buddyStrings(A="ab", B="ba") is True

    def test_example_2(self):
        assert Solution().buddyStrings(A="ab", B="ab") is False

    def test_example_3(self):
        assert Solution().buddyStrings(A="aa", B="aa") is True

    def test_example_4(self):
        assert Solution().buddyStrings(A="aaaaaaabc", B="aaaaaaacb") is True

    def test_example_5(self):
        assert Solution().buddyStrings(A="", B="aa") is False

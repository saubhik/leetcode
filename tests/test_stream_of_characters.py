import unittest

from stream_of_characters import StreamChecker


class TestStreamOfCharacters(unittest.TestCase):
    def test_example_1(self):
        streamChecker = StreamChecker(["cd", "f", "kl"])
        assert streamChecker.query("a") is False
        assert streamChecker.query("b") is False
        assert streamChecker.query("c") is False
        assert streamChecker.query("d") is True
        assert streamChecker.query("e") is False
        assert streamChecker.query("f") is True
        assert streamChecker.query("g") is False
        assert streamChecker.query("h") is False
        assert streamChecker.query("i") is False
        assert streamChecker.query("j") is False
        assert streamChecker.query("k") is False
        assert streamChecker.query("l") is True

    def test_example_2(self):
        streamChecker = StreamChecker(["ab", "ba", "aaab", "abab", "baa"])
        assert streamChecker.query("a") is False
        assert streamChecker.query("a") is False
        assert streamChecker.query("a") is False
        assert streamChecker.query("a") is False
        assert streamChecker.query("a") is False
        assert streamChecker.query("b") is True
        assert streamChecker.query("a") is True
        assert streamChecker.query("b") is True
        assert streamChecker.query("a") is True
        assert streamChecker.query("b") is True
        assert streamChecker.query("b") is False

from unittest import TestCase

from unique_morse_code_words import Solution


class TestUniqueMorseCodeWords(TestCase):
    def test_example_1(self):
        assert (
            Solution().uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
            == 2
        )

from typing import List
from unittest import TestCase


class Solution:
    # Straight Forward.
    # Time Complexity: O(min(n1, n2))
    #   where n1, n2 are the number of characters in word lists 1 and 2.
    # Space Complexity: O(1).
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_idx, char1_idx, word2_idx, char2_idx = 0, 0, 0, 0

        while word1_idx < len(word1) and word2_idx < len(word2):
            if char1_idx == len(word1[word1_idx]) or char2_idx == len(word2[word2_idx]):
                if char1_idx == len(word1[word1_idx]):
                    word1_idx += 1
                    char1_idx = 0

                if char2_idx == len(word2[word2_idx]):
                    word2_idx += 1
                    char2_idx = 0
            elif word1[word1_idx][char1_idx] == word2[word2_idx][char2_idx]:
                char1_idx += 1
                char2_idx += 1
            else:
                return False

        return not ((word1_idx < len(word1)) or (word2_idx < len(word2)))


class TestArrayStringsAreEqual(TestCase):
    def test_example_1(self):
        assert (
            Solution().arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"])
            is True
        )

    def test_example_2(self):
        assert (
            Solution().arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"])
            is False
        )

    def test_example_3(self):
        assert (
            Solution().arrayStringsAreEqual(
                word1=["abc", "d", "defg"], word2=["abcddefg"]
            )
            is True
        )

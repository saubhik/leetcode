from unittest import TestCase

from shortest_word_distance import Solution


class TestShortestDistance(TestCase):
    def test_example_1(self):
        assert (
            Solution().shortestDistance(
                words=["practice", "makes", "perfect", "coding", "makes"],
                word1="coding",
                word2="practice",
            )
            == 3
        )

    def test_example_2(self):
        assert (
            Solution().shortestDistance(
                words=["practice", "makes", "perfect", "coding", "makes"],
                word1="makes",
                word2="coding",
            )
            == 1
        )

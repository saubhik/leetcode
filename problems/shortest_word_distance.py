from typing import List


class Solution:
    # Time Complexity: O(nm) where n = len(words), m = max(len(word))
    # Space Complexity: O(1)
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_dist = float("inf")
        last_pos1 = last_pos2 = None
        for i, word in enumerate(words):
            if word == word1:
                last_pos1 = i
                if last_pos2 is not None:
                    min_dist = min(min_dist, last_pos1 - last_pos2)
            if word == word2:
                last_pos2 = i
                if last_pos1 is not None:
                    min_dist = min(min_dist, last_pos2 - last_pos1)
        return min_dist

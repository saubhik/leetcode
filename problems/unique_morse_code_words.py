from typing import List


class Solution:
    # Time Complexity: O(S).
    # Space Complexity: O(S).
    # where S is the number of characters in list of words.
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        codes = set()
        for word in words:
            codes.add("".join(mapping[ord(ch) - ord("a")] for ch in word))

        return len(codes)

class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    # n -> number of letters
    # k -> number of words
    # w -> average length of word
    # Worst case when w = 1
    def toGoatLatin(self, S: str) -> str:
        words = S.split(sep=" ")  # O(n) time

        n = len(words)  # O(k) time

        # k * O(w) + k^2 * O(1) = O(n) + O(k^2) = O(n^2) worst case
        for i in range(n):
            if words[i][0].lower() in ("a", "e", "i", "o", "u"):  # O(1) time/space
                words[i] += "ma"  # O(w)
            else:
                words[i] = words[i][1:] + words[i][0] + "ma"  # O(w)
            words[i] += "a" * (i + 1)  # O(w)

        return " ".join(words)

from typing import List


class Solution:
    """
    Greedy.
    This is similar to the Official Solution.
    Time Complexity:
        O(nlgn), where n is the length of tokens.
    Space Complexity:
        O(n) for sorting.
    """

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        if not tokens:
            return score

        tokens.sort()

        if P < tokens[0]:
            return score

        n = len(tokens)
        left, right = 0, n - 1

        while left < n and tokens[left] <= P:
            while left < n and tokens[left] <= P:
                score += 1
                P -= tokens[left]
                left += 1

            if score >= 1 and left < right:
                score -= 1
                P += tokens[right]
                right -= 1

        return score

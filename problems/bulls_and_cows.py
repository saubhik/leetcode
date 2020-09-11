from collections import defaultdict


class Solution:
    # Two Pass Solution
    # Time: O(N)
    # Space: O(1), since we only have digits from 0 to 9 as keys.
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bulls = cows = 0
        count = defaultdict(int)

        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                # potential to be cows
                count[secret[i]] += 1

        for i in range(n):
            if secret[i] != guess[i] and count[guess[i]] > 0:
                cows += 1
                count[guess[i]] -= 1

        return f"{bulls}A{cows}B"


class SolutionTwo:
    # One Pass Solution
    # Time: O(N)
    # Space: O(1)
    # If they match, do not do anything. bulls += 1.
    # If they don't match, there are 2 cases:
    # 1. guess[i] can be a cow if it matches secret[j] for j < i.
    # 2. guess[i] can be a cow if it matches secret[j] for j > i.
    #    In other words, secret[i] can lead to cow if it matches guess[j] for j < i.
    #
    # Dry Run:
    # s:1807
    # g:7810
    # Iteration 1:
    # count = {1: 1, 7: -1}
    # Iteration 2:
    # bulls += 1
    # Iteration 3:
    # cows += 1
    # count = {1: 0, 7: -1, 0: 1}
    # Iteration 4:
    # cows += 1
    # count = {1: 0, 7: 0, 0: 0}
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bulls = cows = 0
        count = defaultdict(int)
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if count[guess[i]] > 0:
                    # guess[i] matches a previous secret[j]
                    cows += 1
                if count[secret[i]] < 0:
                    # secret[i] matches a previous cow[j]
                    cows += 1
            count[secret[i]] += 1
            count[guess[i]] -= 1
        return f"{bulls}A{cows}B"

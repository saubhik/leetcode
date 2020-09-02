from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ""
        for perm in permutations(A):
            if perm[0] <= 2:
                if perm[0] == 2:
                    if perm[1] <= 3 and perm[2] <= 5:
                        ans = max(ans, f"{perm[0]}{perm[1]}:{perm[2]}{perm[3]}")
                elif perm[2] <= 5:
                    ans = max(ans, f"{perm[0]}{perm[1]}:{perm[2]}{perm[3]}")

        return ans

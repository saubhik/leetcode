from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    # Time: O(n^4)
    # Space: O(n^2)
    # Get the list of indices which are set in A. Call it indA.
    # Get the list of indices which are set in B. Call it indB.
    # For element of the cartesian product of indA and indB, indA x indB:
    # - get the linear transformation.
    # - update the hash map. (linear transformation -> count)
    # - update the max count (which linear transformation has the maximum count).
    # return the max count.
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)

        indA = []
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    indA.append((i, j))

        indB = []
        for i in range(n):
            for j in range(n):
                if B[i][j] == 1:
                    indB.append((i, j))

        counts = defaultdict(int)
        max_count = 0
        for (iA, jA), (iB, jB) in product(indA, indB):
            counts[(iB - iA, jB - jA)] += 1
            max_count = max(max_count, counts[(iB - iA, jB - jA)])

        return max_count

from typing import List


class Solution:
    # The idea is same as the official solution.
    # Time Complexity: O(n). Two passes at most.
    # Space Complexity: O(1).
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n, min_swaps = len(A), float("inf")
        # Check if all A can be made same as candidate.
        # Check if all B can be made same as candidate.
        # Count the swaps for each case.
        for candidate in (A[0], B[0]):
            possible = True
            swaps_for_A = swaps_for_B = 0
            for i in range(n):
                if A[i] != candidate and B[i] != candidate:
                    possible = False
                    break
                elif A[i] != candidate:
                    swaps_for_A += 1
                elif B[i] != candidate:
                    swaps_for_B += 1
            if possible:
                min_swaps = min(min_swaps, swaps_for_A, swaps_for_B)
        return min_swaps if min_swaps != float("inf") else -1

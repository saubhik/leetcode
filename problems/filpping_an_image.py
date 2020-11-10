from typing import List


class Solution:
    # Time Complexity: O(n * n)
    # Space Complexity: O(1)
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for row in A:
            left, right = 0, n - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left, right = left + 1, right - 1

            for ind in range(n):
                row[ind] = 0 if row[ind] else 1
        return A

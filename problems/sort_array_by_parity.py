from typing import List


class Solution:
    # [3,1,2,4]
    # [2,4,3,1]
    # Time: O(nlogn)
    # Space: O(n)
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)


class SolutionTwo:
    # Quicksort inspired
    # Time: O(n)
    # Space: O(1)
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 == 0 and A[j] % 2 == 1:
                i, j = i + 1, j - 1
            elif A[i] % 2 == 0 and A[j] % 2 == 0:
                i += 1
            elif A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i, j = i + 1, j - 1
            elif A[i] % 2 == 1 and A[j] % 2 == 1:
                j -= 1
        return A

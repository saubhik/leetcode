from typing import List


class Solution:
    # 2-D Binary Search.
    # Time Complexity: O(lg(m) + lg(n))
    # Space Complexity: O(1).
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # Binary search in first column.
        lo, hi = 0, m
        while hi - lo > 1:
            mid = hi - (hi - lo) // 2
            if target < matrix[mid][0]:
                hi = mid
            elif target > matrix[mid][0]:
                lo = mid
            else:
                return True

        row = lo

        # Binary search in the row.
        lo, hi = 0, n
        while hi - lo > 1:
            mid = hi - (hi - lo) // 2
            if target < matrix[row][mid]:
                hi = mid
            elif target > matrix[row][mid]:
                lo = mid
            else:
                return True

        col = lo

        return matrix[row][col] == target

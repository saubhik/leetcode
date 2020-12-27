from typing import List
from unittest import TestCase


class Solution:
    # Official Solution calls this Simulation.
    # Time Complexity: O(mn).
    # Space Complexity: O(1) additional space.
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        ans, i, j, up = [], 0, 0, True
        while 0 <= i < m and 0 <= j < n:
            print(f"i={i},j={j},up={up}")
            ans.append(matrix[i][j])
            last_i, last_j, last_up = i, j, up
            delta = -1 if up else 1
            i, j = last_i + delta, last_j - delta
            if not 0 <= i < m:
                # Go right on same row.
                up = not last_up
                i, j = last_i, last_j + 1
            if not 0 <= j < n:
                # Go down on same column.
                up = not last_up
                i, j = last_i + 1, last_j
        return ans


class TestFindDiagonalOrder(TestCase):
    """
    1 2 3
    4 5 6
    7 8 9

    DiagonalOrder: 1,2,4,7,5,3,6,8,9
    (0,0)
    (0,1),(1,0)
    (2,0),(1,1),(0,2)
    (1,2),(2,1)
    (2,2)
    """

    def test_example_1(self):
        assert Solution().findDiagonalOrder(
            matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ) == [1, 2, 4, 7, 5, 3, 6, 8, 9]

    def test_example_2(self):
        assert Solution().findDiagonalOrder(matrix=[]) == []

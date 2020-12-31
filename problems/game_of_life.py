from typing import List
from unittest import TestCase


class Solution:
    # Straightforward with special coding for changed values to use O(1) space.
    # Time Complexity: O(mn) time.
    # Space Complexity: O(1) space.
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for nbr_i, nbr_j in [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j + 1),
                    (i + 1, j + 1),
                    (i + 1, j),
                    (i + 1, j - 1),
                    (i, j - 1),
                ]:
                    if 0 <= nbr_i < m and 0 <= nbr_j < n:
                        if board[nbr_i][nbr_j] in (2, 0):
                            count += 0
                        else:
                            count += 1

                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = -1

                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] = (
                    1 if board[i][j] == 2 else 0 if board[i][j] == -1 else board[i][j]
                )


class TestGameOfLife(TestCase):
    def test_example_1(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        Solution().gameOfLife(board=board)
        assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    def test_example_2(self):
        board = [[1, 1], [1, 0]]
        Solution().gameOfLife(board=board)
        assert board == [[1, 1], [1, 1]]

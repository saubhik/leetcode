from typing import List


class Solution:
    # Time: O(2^N), exponential due to enumeration algorithm.
    # Space: O(N) for the recursive call stack, O(2^N) for output list.
    # Additional space required by algorithm is O(N).
    # DFS based solution.
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]

        ans = []

        def dfs(number: int, last_digit: int, length: int):
            if length == N:
                ans.append(number)
                return

            for ld in {last_digit - K, last_digit + K}:
                if 0 <= ld <= 9:
                    dfs(number=number * 10 + ld, last_digit=ld, length=length + 1)

        for i in range(1, 10):
            dfs(number=i, last_digit=i, length=1)

        return ans

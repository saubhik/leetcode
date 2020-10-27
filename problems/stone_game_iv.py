class Solution:
    # DFS with memoization.
    # Time Complexity: O(n * sqrt(n)), since we spend O(sqrt(n)) at most for each dfs
    #   call, and there are O(n) dfs call in total.
    # Space Complexity: O(n) since we need hashmap, and also dfs recursion stack.
    def winnerSquareGame(self, n: int) -> bool:
        cache = {}

        def _dfs(num: int) -> bool:
            if num in cache:
                return cache[num]

            i = 1
            while i * i <= num:
                _num = num - i * i
                if _dfs(num=_num) is False:
                    cache[num] = True
                    return True
                i += 1

            cache[num] = False
            return False

        return _dfs(num=n)

    def winnerSquareGameDP(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if dp[i - k * k] is False:
                    dp[i] = True
                    break
                k += 1
        return dp[n]

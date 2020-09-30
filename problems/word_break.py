from typing import List


class OfficialSolution:
    def wordBreakApproach1(self, s: str, wordDict: List[str]) -> bool:
        """
        == Approach 1: Brute Force ==
        == Algorithm ==
        The naive approach to solve this problem is to use recursion and backtracking.
        For finding the solution, we check every possible prefix of that string in the
        dictionary of words. If it is found in the dictionary, then the recursive
        function is called for the remaining portion of that string. And, if in some
        function call it is found that the complete string is in dictionary, then it
        will return true.

        == Complexity Analysis ==
        - Time Complexity: O(n^n). Consider the worst case where s = "aaaaaaa" and every
            prefix of s is present in the dictionary of words, then the recursion tree
            can grow upto n^n.
        - Space Complexity: O(n). The depth of the recursion tree can go upto n.
        """
        n = len(s)

        def backtrack(st=0):
            if st > n:
                return True

            for i in range(st + 1, n + 2):
                if s[st:i] in wordDict:
                    if backtrack(st=i) is True:
                        return True

            return False

        return backtrack()

    def wordBreakApproach2(self, s: str, wordDict: List[str]) -> bool:
        """
        == Approach 2: Recursion with memoization ==
        == Algorithm ==
        In the previous approach, we can see that many subproblems were redundant, i.e.
        we were calling the recursive function multiple times for a particular string.
        To avoid this we can use memoization method, where an array memo is used to
        store the result of the subproblems. Now, when the function is called again for
        a particular string, value will be fetches and returned using the memo array, if
        its value has been already evaluated.

        With memoization many redundant subproblems are avoided and recursion tree is
        pruned and thus it reduces the time complexity by a large factor.

        == Complexity Analysis ==
        - Time Complexity: O(n^2). Size of the recursion tree can go up to n^2.
        - Space Complexity: O(n). The depth of recursion tree can go up to n.
        """
        n = len(s)
        memo = [None] * (n + 2)

        def backtrack(st=0):
            if memo[st] is not None:
                return memo[st]

            if st > n:
                memo[st] = True
                return True

            for i in range(st + 1, n + 2):
                if s[st:i] in wordDict:
                    if backtrack(st=i) is True:
                        memo[st] = True
                        return True

            memo[st] = False
            return False

        return backtrack()

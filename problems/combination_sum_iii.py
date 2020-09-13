from itertools import combinations
from typing import List


class Solution:
    # Using itertools.combinations
    # Time: O(k * 9!/(k!(9-k)!)) = O(k * 9Ck), k must be less than 9, so O(1) time.
    # Space: O(1) space.
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        for comb in combinations(range(1, 10), k):
            if sum(comb) == n:
                ans.append(list(comb))
        return ans


class SolutionTwo:
    # Without using library functions.
    # [[]]
    # [[], [1]]
    # [[], [1], [2], [1,2]]
    # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3],
    #  [4], [1,4], [2,4], [1,2,4], [3,4], ~[1,3,4]~, ~[2,3,4]~, ~[1,2,3,4]~]
    #
    # Straight-Forward Enumeration Technique.
    # Similar to enumerating all subsets.
    # Time: O(1+2+4+8+16+...upper bounded by 2^9) = O(1)
    # Space: O(1+2+4+...upper bounded by 2^9) = O(1)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(num: int = 1, combs: List[List[int]] = None):
            if combs is None:
                combs = [[]]

            if num > min(n, 9):
                return

            new_combs = []
            for comb in combs:
                if len(comb) < k and sum(comb) + num <= n:
                    new_comb = comb + [num]
                    if sum(new_comb) == n and len(new_comb) == k:
                        ans.append(new_comb)
                    else:
                        new_combs.append(new_comb)

            combs.extend(new_combs)

            helper(num=num + 1, combs=combs)

        helper()

        return ans


class SolutionThree:
    # BackTracking.
    #
    # The problem asks us to come up with some fixed-length combinations that meet
    # certain conditions.
    #
    # In backtracking, we try to fill the combination one element at a step. Each
    # choice we make at certain step might lead us to a final solution. If not, we
    # simply revisit the choice and try out other choices, i.e. backtrack.
    #
    # Dry Run:
    # Execution context: backtrack(remain=7, comb=[], next_start=0)
    # Calls:
    # backtrack(6, [1], 1)
    # backtrack(5, [2], 2)
    # backtrack(4, [3], 3)
    # backtrack(3, [4], 4)
    # backtrack(2, [5], 5)
    # backtrack(1, [6], 6)
    # backtrack(0, [7], 7)  --> eventually return
    # backtrack(-1, [8], 8) --> eventually return
    # backtrack(-2, [9], 9) --> eventually return
    #
    # Execution context: backtrack(remain=6, comb=[1], next_start=1)
    # Calls:
    # backtrack(4, [1,2], 2)
    # backtrack(3, [1,3], 3)
    # backtrack(2, [1,4], 4)
    # backtrack(1, [1,5], 5)
    # backtrack(0, [1,6], 6)  --> eventually return
    # backtrack(-1, [1,7], 7) --> eventually return
    # backtrack(-2, [1,8], 8) --> eventually return
    #
    # ...
    #
    # Idea:
    # Backtracking is like DFS traversal of a tree.
    # Showing 3 numbers for simplicity.
    #
    #            ROOT
    #             |
    #       ---------------
    #      |         |     |
    #      1         2     3
    #      |         |
    #   -------      3
    #   |     |
    #   2     3
    #   |
    #   3
    #
    # The path of the DFS traversal gives us the candidate combination.
    # At each level you add one more number to the combination (candidate solution).
    # When you're done processing the leaf, you're going one level up, i.e. you're
    # backtracking.
    #
    # Complexity Analysis:
    # Time:
    # Time complexity is number of nodes we need to process.
    # The first number can be chosen in 9 ways.
    # The second number can be chosen in 8 ways.
    # and so on...
    # Number of nodes is then 9Pk = 9!/(9-k)!.
    # When remain==0 and len(comb) == k we are copying the node which is O(k) time.
    # So time complexity is O(k * 9Pk).
    #
    # Space:
    # At any point of time, the max depth of recursion call stack is O(k).
    # To store combination (path), the maximum storage required is O(k).
    # Overall, space complexity = O(k)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(remain: int, comb: List[int], next_start: int):
            if remain == 0 and len(comb) == k:
                ans.append(list(comb))
                return

            if remain < 0 or len(comb) == k:
                return

            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remain=remain - i - 1, comb=comb, next_start=i + 1)
                comb.pop()

        backtrack(remain=n, comb=[], next_start=0)

        return ans


class SolutionFour:
    # DFS-style BackTracking
    # BackTracking is essentially DFS traversal of a tree representation.
    # See comment of SolutionThree for details.
    #
    # DFS with constraints:
    # 1. Child node values need to be in range [parent_node_value + 1, 9]
    # 2. Maximum Path Sum is n
    # 3. Maximum Path Length is k
    #
    # When path sum is n and path length is k, store it as one of the solutions.
    #
    # path + [child_node] returns a new list, and this is O(k) time.
    # Time: O(k * 9Pk)
    # Space: O(k)
    # Same complexity analysis as SolutionThree.
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(
            path: List[int] = None, node: int = 1, path_sum: int = 0, path_len: int = 0
        ):
            if path is None:
                path = []

            if path_sum == n and path_len == k:
                ans.append(path)
                return

            if path_sum > n or path_len > k:
                return

            for child_node in range(node, 10):
                dfs(
                    path=path + [child_node],
                    node=child_node + 1,
                    path_sum=path_sum + child_node,
                    path_len=path_len + 1,
                )

        dfs()

        return ans

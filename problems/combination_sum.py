from typing import List, Optional


class Solution:
    # candidates = [2,3,6,7], target = 7
    # Straight Forward Backtracking.
    # Time Complexity: Exponential.
    # Space Complexity: Additional storage required is the maximum storage required for
    #   current_combination, which is upper bounded by 500 according to problem
    #   constraints. (Case: 1 repeating 500 times for a maximum target of 500)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        def backtrack(
            current_index: int = 0,
            current_sum: int = 0,
            current_combination: Optional[List[int]] = None,
            combinations: Optional[List[int]] = None,
        ):
            if current_combination is None:
                current_combination = []

            if combinations is None:
                combinations = []

            if current_sum == target:
                combinations.append(current_combination.copy())
            else:
                for index in range(current_index, n):
                    if current_sum + candidates[index] <= target:
                        current_combination.append(candidates[index])
                        backtrack(
                            current_index=index,
                            current_sum=current_sum + candidates[index],
                            current_combination=current_combination,
                            combinations=combinations,
                        )
                        current_combination.pop()

            return combinations

        return backtrack()


class OfficialSolution:
    """
    == Overview ==
    This is one of the problems in the series of combination sum. They all can be solved
    with the same algorithm, i.e. backtracking.
    Before tackling this problem, we would recommend one to start with another almost
    identical problem called Combination Sum III, which is arguably easier and once can
    tweak the solution a bit to solve this problem.
    For the sake of this article, we will present the backtracking algorithm.
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        == Approach 1: Backtracking ==
        == Intuition ==
        As a reminder, backtracking is a general algorithm for finding all (or some)
        solutions to some computational problems. The idea is that it incrementally
        builds candidates to the solutions, and abandons a candidate ("backtrack") as
        soon as it determines that this candidate cannot lead to a final solution.
        Specially, to our problem, we could incrementally build the combination, and
        once we find the current combination is not valid, we backtrack and try another
        option.

        To demonstrate the idea, we showcase how it works with a concrete example:
        For the given list of candidates [3,4,5] and a target sum 8, we start off from
        empty combination [] as indicated as the root node in the above graph.
        - Each node represents an action we take at a step, and within the node we also
        indicate the combination we build so far.
        - From top to down, at each level we descend, we add one more element into the
        current combination.
        - Some nodes would sum up to the target value, they are the desired combination
        solutions.
        - Some nodes exceed the target value. Since all the candidates are positive
        value, there is no way we could bring the sum down to the target value, if we
        explore further.
        - At any instant, we can only be at one of the nodes. When we backtrack, we are
        moving from a node to its parent node.

        An important detail on choosing the next number for the combination is that we
        select the candidates in order, where the total candidates are treated as a
        list. Once a candidate is added into the current combination, we will not look
        back to all the previous candidates in the next explorations.

        To demonstrate the idea, let us zoom in a node to see how we can choose the next
        numbers.
        - When we are at the node of [4], the precedent candidates are [3], and the
        candidates followed are [4,5].
        - We don't add the precedent numbers into the current node, since they would
        have been explored in the nodes in the left part of the subtree, i.e. the node
        of [3].
        - Even through we have already the element 4 in the current combination, we are
        giving the element another chance in the next exploration, since the combination
        can contain duplicate numbers.
        - As a result, we would branch out in two directions, by adding the element 4
        and 5 respectively into the current combination.

        == Algorithm ==
        As one can see, the above backtracking algorithm is unfolded as a DFS (Depth-
        First Search) tree traversal which is often implemented with recursion.
        Here we define a recursive function of backtrack(remain, comb, start) which
        populates the combinations, starting from the current combination comb, the
        remaining sum to fulfill remain and the current cursor start to the list of
        candidates.
        - For the first base case of the recursive function, if the remain==0, i.e. we
        fulfill the desired target sum, therefore we can add the current combination
        to the final list.
        - As another base case, if remain < 0, i.e. we exceed the target value, we will
        cease the exploration here.
        - Other than the above two base cases, we would then continue to explore the
        sublist of candidates as [start, ..., n]. For each of the candidate, we invoke
        the recursive function itself with updated parameters.
            - Specifically, we add the current candidate into the combination.
            - With the added candidate, we now have less sum to fulfill, i.e.
                remain - candidate.
            - For the next exploration, still we start from the current cursor start.
            - At the end of each exploration, we backtrack by popping out the candidate
                out of the combination.

        == Complexity Analysis ==
        Let N be the number of candidates, T be the target value, and M be the minimal
        value among the candidates.

        Time Complexity: O(N ^ (T/M + 1)).
            - As we illustrated before, the execution of the backtracking is unfolded as
            a DFS traversal in a n-ary tree. The total number of steps during the
            backtracking would be the number of nodes in the tree.
            - At each node, it takes a constant time to process, except the leaf nodes
            which could take a linear time to make a copy of combination. So we can say
            that the time complexity is linear to the number of nodes of the execution
            tree.
            - Here we provide a loose upper bound on the number of nodes.
                - First of all, the fan-out of each node would be bounded to N, i.e. the
                total number of candidates.
                - The maximal depth of the tree, would be T/M, where we keep on adding
                the smallest element to the combination.
                - As we know, the maximal number of nodes in N-ary tree of T/M height
                would be N ^ (T/M + 1).
            - Note that, the actual number of nodes in the execution tree would be much
            smaller than the upper bound, since the fan-out of the nodes are decreasing
            level by level.

        Space Complexity: Additional space is O(T/M).
            - We implement the algorithm in recursion, which consumes some additional
            memory in the function call stack.
            - The number of recursive calls can pile up to T/M, where we keep on adding
            the smallest element to the combination. As a result, the space overhead of
            the recursion is O(T/M).
            - In addition, we keep a combination of numbers during the execution, which
            requires at most O(T/M) space as well.
            - To sum up, the total space complexity of the algorithm would be O(T/M).
            - Note that, we did not take into the account the space used to hold the
            final results for the space complexity.
        """
        results = []

        def backtrack(remain: int, comb: List[int], start: int):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain=remain - candidates[i], comb=comb, start=i)
                comb.pop()

        backtrack(remain=target, comb=[], start=0)

        return results

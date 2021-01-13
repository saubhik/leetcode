from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        paths = 0

        if root is None:
            return paths

        queue = deque([(root, [])])
        while queue:
            node, sums = queue.popleft()

            sums.append(0)
            for _idx in range(len(sums)):
                sums[_idx] += node.val
                if sums[_idx] == sum:
                    paths += 1

            if node.left is not None:
                queue.append((node.left, sums.copy()))

            if node.right is not None:
                queue.append((node.right, sums.copy()))

        return paths


class SolutionTwo:
    # prefix sum technique - prefix_sum and hash_map
    # O(n) time, O(n) additional space
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefix_sum = 0
        count = 0
        seen_count = defaultdict(int, {0: 1})

        def _dfs(node):
            if node is None:
                return
            nonlocal prefix_sum, count
            prefix_sum += node.val
            count += seen_count[prefix_sum - sum]
            seen_count[prefix_sum] += 1
            _dfs(node=node.left)
            _dfs(node=node.right)
            seen_count[prefix_sum] -= 1
            prefix_sum -= node.val

        _dfs(node=root)
        return count

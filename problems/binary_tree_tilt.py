# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Straight Forward DFS.
    # Time Complexity: O(n).
    # Space Complexity: O(n).
    def findTilt(self, root: TreeNode) -> int:
        cum_tilt = 0

        def _dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left_sum = 0
            if node.left:
                left_sum = _dfs(node=node.left)

            right_sum = 0
            if node.right:
                right_sum = _dfs(node=node.right)

            nonlocal cum_tilt
            cum_tilt += abs(left_sum - right_sum)

            return left_sum + right_sum + node.val

        _dfs(node=root)

        return cum_tilt

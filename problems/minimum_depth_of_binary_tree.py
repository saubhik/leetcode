# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Straight Forward DFS
    # Time Complexity: O(n) where n is the number of nodes.
    # Space Complexity: O(n) in worst case, where n is the number of nodes.
    def minDepth(self, root: Optional[TreeNode], depth: int = 1) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return depth

        left_depth = right_depth = float("inf")

        if root.left:
            left_depth = self.minDepth(root=root.left, depth=depth + 1)

        if root.right:
            right_depth = self.minDepth(root=root.right, depth=depth + 1)

        return min(left_depth, right_depth)

    def minDepthBFS(self, root: Optional[TreeNode], depth: int = 1) -> int:
        # Straight Forward BFS
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()

            if not node.left and not node.right:
                return level

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

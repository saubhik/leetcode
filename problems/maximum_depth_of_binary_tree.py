# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Straight Forward DFS.
    # Time Complexity: O(n).
    # Space Complexity: O(h) = O(n) in worst case.
    def maxDepth(self, root: Optional[TreeNode], height: int = 0) -> int:
        return (
            max(
                self.maxDepth(root=root.left, height=height + 1),
                self.maxDepth(root=root.right, height=height + 1),
            )
            if root is not None
            else height
        )

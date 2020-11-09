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
    # Space Complexity: O(n).
    def maxAncestorDiff(
        self,
        root: TreeNode,
        curr_max: Optional[int] = None,
        curr_min: Optional[int] = None,
    ) -> int:
        if curr_max is None:
            curr_max = root.val

        if curr_min is None:
            curr_min = root.val

        if root is None:
            return curr_max - curr_min

        curr_max = max(curr_max, root.val)
        curr_min = min(curr_min, root.val)

        left = self.maxAncestorDiff(
            root=root.left, curr_max=curr_max, curr_min=curr_min
        )

        right = self.maxAncestorDiff(
            root=root.right, curr_max=curr_max, curr_min=curr_min
        )

        return max(left, right)

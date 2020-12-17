# Definition for a binary tree node.
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(h) = O(n) in worst case.
    def isValidBST(
        self, root: TreeNode, min_val: int = float("-inf"), max_val: int = float("inf")
    ) -> bool:
        return root is None or (
            min_val < root.val < max_val
            and self.isValidBST(root=root.left, min_val=min_val, max_val=root.val)
            and self.isValidBST(root=root.right, min_val=root.val, max_val=max_val)
        )


class TestSolution(TestCase):
    def test_example_1(self):
        root = TreeNode(val=2)
        root.left = TreeNode(val=1)
        root.right = TreeNode(val=3)

        assert Solution().isValidBST(root=root) is True

    def test_example_2(self):
        root = TreeNode(val=5)
        root.left = TreeNode(val=1)
        root.right = TreeNode(val=4)
        root.right.left = TreeNode(val=3)
        root.right.right = TreeNode(val=6)

        assert Solution().isValidBST(root=root) is False

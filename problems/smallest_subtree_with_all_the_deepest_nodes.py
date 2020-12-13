# Definition for a binary tree node.
from typing import Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Straight Forward DFS.
    # Time Complexity: O(n).
    # Space Complexity: O(h) = O(n) in worst case.
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        ans: Optional[TreeNode] = None
        max_depth: int = -1

        def _dfs(node: TreeNode, depth: int = 0):
            nonlocal max_depth, ans

            if not node:
                if depth > max_depth:
                    max_depth = depth
                return depth

            max_depth_left = _dfs(node=node.left, depth=depth + 1)
            max_depth_right = _dfs(node=node.right, depth=depth + 1)

            if max_depth_left == max_depth_right == max_depth:
                ans = node

            return max(max_depth_left, max_depth_right)

        _dfs(node=root)

        return ans


class TestSolution(TestCase):
    def test_example_1(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=5)
        root.right = TreeNode(val=1)
        root.left.left = TreeNode(val=6)
        root.left.right = TreeNode(val=2)
        root.left.right.left = TreeNode(val=7)
        root.left.right.right = TreeNode(val=4)
        root.right.left = TreeNode(val=0)
        root.right.right = TreeNode(val=8)

        subtree = Solution().subtreeWithAllDeepest(root=root)

        assert subtree.val == 2
        assert subtree.left.val == 7
        assert subtree.right.val == 4
        assert subtree.left.left is None
        assert subtree.left.right is None
        assert subtree.right.left is None
        assert subtree.right.right is None

    def test_example_2(self):
        root = TreeNode(val=1)
        assert Solution().subtreeWithAllDeepest(root=root) == root

    def test_example_3(self):
        root = TreeNode(val=0)
        root.left = TreeNode(val=1)
        root.right = TreeNode(val=3)
        root.left.right = TreeNode(val=2)

        subtree = Solution().subtreeWithAllDeepest(root=root)

        assert subtree.val == 2
        assert subtree.left is None
        assert subtree.right is None

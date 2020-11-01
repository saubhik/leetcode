# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first: Optional[TreeNode] = None
        second: Optional[TreeNode] = None

        def _check(prev: Optional[TreeNode], node: TreeNode):
            nonlocal first, second
            if prev and node.val < prev.val:
                second = node
                if first is None:
                    first = prev

        node, prev = root, None
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = node
                    node = node.left
                else:
                    # For processing the middle node
                    _check(prev=prev, node=node)
                    prev = node
                    predecessor.right = None
                    node = node.right
            else:
                # For processing the left and right nodes.
                _check(prev=prev, node=node)
                prev = node
                node = node.right

        first.val, second.val = second.val, first.val

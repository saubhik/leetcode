from collections import deque
from typing import Optional
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Straight-Forward BFS.
    # One queue with sentinel to track level endings.
    # Time Complexity: O(n).
    # Space Complexity: O(D) where D is tree diameter = O(n) in worst case.
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque([root, None])

        while queue:
            node = queue.popleft()

            if node is u:
                return queue.popleft()

            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                queue.append(None)

        return None


class TestFindNearestRightNode(TestCase):
    def test_example_1(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=2)
        root.left.right = TreeNode(val=4)
        root.right = TreeNode(val=3)
        root.right.left = TreeNode(val=5)
        root.right.right = TreeNode(val=6)

        assert (
            Solution().findNearestRightNode(root=root, u=root.left.right)
            is root.right.left
        )

    def test_example_2(self):
        root = TreeNode(val=3)
        root.right = TreeNode(val=4)
        root.right.left = TreeNode(val=2)

        assert Solution().findNearestRightNode(root=root, u=root.right.left) is None

    def test_example_3(self):
        root = TreeNode(val=1)

        assert Solution().findNearestRightNode(root=root, u=root) is None

    def test_example_4(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=4)
        root.right = TreeNode(val=2)
        root.right.right = TreeNode(val=1)

        assert Solution().findNearestRightNode(root=root, u=root.left) is root.right

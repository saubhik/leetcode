from unittest import TestCase


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
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node: TreeNode) -> (int, bool):
            if node is None:
                return 0, True

            left_height, left_balanced = height(node=node.left)
            right_height, right_balanced = height(node=node.right)

            return (
                max(left_height, right_height) + 1,
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1,
            )

        _, is_balanced = height(node=root)
        return is_balanced


class TestIsBalanced(TestCase):
    def test_example_1(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=9)
        root.right = TreeNode(val=20)
        root.right.left = TreeNode(val=15)
        root.right.right = TreeNode(val=7)

        assert Solution().isBalanced(root=root) is True

    def test_example_2(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=2)
        root.right = TreeNode(val=2)
        root.left.left = TreeNode(val=3)
        root.left.right = TreeNode(val=3)
        root.left.left.left = TreeNode(val=4)
        root.left.left.right = TreeNode(val=4)

        assert Solution().isBalanced(root=root) is False

    def test_example_3(self):
        assert Solution().isBalanced(root=None) is True

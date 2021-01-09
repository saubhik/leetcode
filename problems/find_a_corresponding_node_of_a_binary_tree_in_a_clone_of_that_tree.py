from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Straightforward DFS for problem without repeated values.
    # Time Complexity: O(|V|).
    # Space Complexity: O(log|V|) or O(|V|) in worst case.
    def getTargetCopy(
            self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def _dfs(node: TreeNode):
            if not node or node.val == target.val:
                return node
            return _dfs(node=node.left) or _dfs(node=node.right)

        return _dfs(node=cloned)


class SolutionTwo:
    # Modified DFS for both trees.
    # Time Complexity: O(|V|).
    # Space Complexity: O(log|V|) or O(|V|) in worst case.
    def getTargetCopy(
            self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def _dfs(original_node: TreeNode, cloned_node: TreeNode):
            if not original_node or original_node is target:
                return cloned_node
            return _dfs(
                original_node=original_node.left, cloned_node=cloned_node.left
            ) or _dfs(original_node=original_node.right, cloned_node=cloned_node.right)

        return _dfs(original_node=original, cloned_node=cloned)


class TestGetTargetCopy(TestCase):
    def test_example_1(self):
        root = TreeNode(x=7)
        root.left = TreeNode(x=4)
        root.right = TreeNode(x=3)
        root.right.left = TreeNode(x=6)
        root.right.right = TreeNode(x=19)

        clone = TreeNode(x=7)
        clone.left = TreeNode(x=4)
        clone.right = TreeNode(x=3)
        clone.right.left = TreeNode(x=6)
        clone.right.right = TreeNode(x=19)

        target = root.right
        expected = clone.right

        assert (
                Solution().getTargetCopy(original=root, cloned=clone, target=target)
                is expected
        )
        assert (
                Solution().getTargetCopy(original=root, cloned=clone, target=target)
                is expected
        )

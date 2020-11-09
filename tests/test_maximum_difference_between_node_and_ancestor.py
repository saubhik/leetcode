from unittest import TestCase

from maximum_difference_between_node_and_ancestor import Solution, TreeNode


class TestMaximumDifferenceBetweenNodeAndAncestor(TestCase):
    def test_example_1(self):
        root = TreeNode(val=8)
        root.left = TreeNode(val=3)
        root.left.left = TreeNode(val=1)
        root.left.right = TreeNode(val=6)
        root.left.right.left = TreeNode(val=4)
        root.left.right.right = TreeNode(val=7)
        root.right = TreeNode(val=10)
        root.right.right = TreeNode(val=14)
        root.right.right.left = TreeNode(val=13)

        assert Solution().maxAncestorDiff(root=root) == 7

    def test_example_2(self):
        root = TreeNode(val=1)
        root.right = TreeNode(val=2)
        root.right.right = TreeNode(val=0)
        root.right.right.left = TreeNode(val=3)

        assert Solution().maxAncestorDiff(root=root) == 3

from unittest import TestCase

from range_sum_BST import Solution, TreeNode


class TestRangeSumBST(TestCase):
    def test_example_1(self):
        root = TreeNode(val=10)
        root.left = TreeNode(val=5)
        root.left.left = TreeNode(val=3)
        root.left.right = TreeNode(val=7)
        root.right = TreeNode(val=15)
        root.right.right = TreeNode(val=18)

        assert Solution().rangeSumBST(root=root, low=7, high=15) == 32

    def test_example_2(self):
        root = TreeNode(val=10)
        root.left = TreeNode(val=5)
        root.left.left = TreeNode(val=3)
        root.left.left.left = TreeNode(val=1)
        root.left.right = TreeNode(val=7)
        root.left.right.left = TreeNode(val=6)
        root.right = TreeNode(val=15)
        root.right.left = TreeNode(val=13)
        root.right.right = TreeNode(val=18)

        assert Solution().rangeSumBST(root=root, low=6, high=10) == 23

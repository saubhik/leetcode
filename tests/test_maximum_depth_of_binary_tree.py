from unittest import TestCase

from maximum_depth_of_binary_tree import Solution, TreeNode


class TestMaximumDepthOfBinaryTree(TestCase):
    def test_example_1(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=9)
        root.right = TreeNode(val=20)
        root.right.left = TreeNode(val=15)
        root.right.right = TreeNode(val=7)

        assert Solution().maxDepth(root=root) == 3

    def test_example_2(self):
        root = TreeNode(val=1)
        root.right = TreeNode(val=2)

        assert Solution().maxDepth(root=root) == 2

    def test_example_3(self):
        assert Solution().maxDepth(root=None) == 0

    def test_example_4(self):
        assert Solution().maxDepth(root=TreeNode(val=0)) == 1

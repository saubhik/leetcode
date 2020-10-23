import unittest

from minimum_depth_of_binary_tree import Solution, TreeNode


class TestMinimumDepthOfBinaryTree(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=9)
        root.right = TreeNode(val=20)
        root.right.left = TreeNode(val=15)
        root.right.right = TreeNode(val=7)
        assert Solution().minDepth(root=root) == 2
        assert Solution().minDepthBFS(root=root) == 2

    def test_example_2(self):
        root = TreeNode(val=2)
        root.right = TreeNode(val=3)
        root.right.right = TreeNode(val=4)
        root.right.right.right = TreeNode(val=5)
        root.right.right.right.right = TreeNode(val=6)
        assert Solution().minDepth(root=root) == 5
        assert Solution().minDepthBFS(root=root) == 5

    def test_example_3(self):
        assert Solution().minDepth(root=None) == 0
        assert Solution().minDepthBFS(root=None) == 0

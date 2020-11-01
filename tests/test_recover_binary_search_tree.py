import unittest

from recover_binary_search_tree import Solution, TreeNode


class TestRecoverBinarySearchTree(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=3)
        root.left.right = TreeNode(val=2)
        Solution().recoverTree(root=root)
        assert root.val == 3
        assert root.left.val == 1
        assert root.left.right.val == 2

    def test_example_2(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=1)
        root.right = TreeNode(val=4)
        root.right.left = TreeNode(val=2)
        Solution().recoverTree(root=root)
        assert root.val == 2
        assert root.left.val == 1
        assert root.right.val == 4
        assert root.right.left.val == 3

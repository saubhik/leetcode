import unittest

from sum_of_root_to_leaf_binary_numbers import Solution, TreeNode


class TestSumOfRootToLeafBinaryNumbers(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=0)
        root.left.left = TreeNode(val=0)
        root.left.right = TreeNode(val=1)
        root.right = TreeNode(val=1)
        root.right.left = TreeNode(val=0)
        root.right.right = TreeNode(val=1)

        assert Solution().sumRootToLeaf(root=root) == 22

    def test_example_2(self):
        assert Solution().sumRootToLeaf(root=None) == 0

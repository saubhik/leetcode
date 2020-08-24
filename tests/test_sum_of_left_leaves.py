import unittest

from sum_of_left_leaves import TreeNode, Solution


class TestSumOfLeftLeaves(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=9)
        root.right = TreeNode(val=20)
        root.right.left = TreeNode(val=15)
        root.right.right = TreeNode(val=7)
        assert Solution().sumOfLeftLeaves(root=root) == 24

    def test_example_2(self):
        root = TreeNode(val=1)
        assert Solution().sumOfLeftLeaves(root=root) == 0

    def test_example_3(self):
        assert Solution().sumOfLeftLeaves(root=None) == 0

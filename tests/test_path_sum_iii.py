import unittest

from path_sum_iii import Solution, SolutionTwo, TreeNode


class TestPathSumIII(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=10)
        root.left = TreeNode(val=5)
        root.left.left = TreeNode(val=3)
        root.left.left.left = TreeNode(val=3)
        root.left.left.right = TreeNode(val=-2)
        root.left.right = TreeNode(val=2)
        root.left.right.right = TreeNode(val=1)
        root.right = TreeNode(val=-3)
        root.right.right = TreeNode(val=11)

        assert Solution().pathSum(root=root, sum=8) == 3

    def test_example_2(self):
        root = TreeNode(val=10)
        root.left = TreeNode(val=5)
        root.left.left = TreeNode(val=3)
        root.left.left.left = TreeNode(val=3)
        root.left.left.right = TreeNode(val=-2)
        root.left.right = TreeNode(val=2)
        root.left.right.right = TreeNode(val=1)
        root.right = TreeNode(val=-3)
        root.right.right = TreeNode(val=11)

        assert SolutionTwo().pathSum(root=root, sum=8) == 3

    def test_example_3(self):
        root = TreeNode(val=1)
        assert SolutionTwo().pathSum(root=root, sum=0) == 0

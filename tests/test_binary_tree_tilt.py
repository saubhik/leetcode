from unittest import TestCase

from binary_tree_tilt import Solution, TreeNode


class TestBinaryTreeTilt(TestCase):
    def test_example_1(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=2)
        root.right = TreeNode(val=3)

        assert Solution().findTilt(root=root) == 1

    def test_example_2(self):
        root = TreeNode(val=4)
        root.left = TreeNode(val=2)
        root.left.left = TreeNode(val=3)
        root.left.right = TreeNode(val=5)
        root.right = TreeNode(val=9)
        root.right.right = TreeNode(val=7)

        assert Solution().findTilt(root=root) == 15

    def test_example_3(self):
        root = TreeNode(val=21)
        root.left = TreeNode(val=7)
        root.left.left = TreeNode(val=1)
        root.left.left.left = TreeNode(val=3)
        root.left.left.right = TreeNode(val=3)
        root.left.right = TreeNode(val=1)
        root.right = TreeNode(val=14)
        root.right.left = TreeNode(val=2)
        root.right.right = TreeNode(val=2)

        assert Solution().findTilt(root=root) == 9

    def test_example_4(self):
        assert Solution().findTilt(root=None) == 0

from unittest import TestCase

from increasing_order_search_tree import Solution, TreeNode


class TestIncreasingOrderSearchTree(TestCase):
    def test_example_1(self):
        root = TreeNode(val=5)
        root.left = TreeNode(val=3)
        root.left.left = TreeNode(val=2)
        root.left.left.left = TreeNode(val=1)
        root.left.right = TreeNode(val=4)
        root.right = TreeNode(val=6)
        root.right.right = TreeNode(val=8)
        root.right.right.left = TreeNode(val=7)
        root.right.right.right = TreeNode(val=9)

        node = Solution().increasingBST(root=root)

        for i in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            assert node.val == i
            assert node.left is None
            node = node.right

    def test_example_2(self):
        root = TreeNode(val=5)
        root.left = TreeNode(val=1)
        root.right = TreeNode(val=7)

        node = Solution().increasingBST(root=root)

        for expected in (1, 5, 7):
            assert node.val == expected
            assert node.left is None
            node = node.right

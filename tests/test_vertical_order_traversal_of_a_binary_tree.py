import unittest

from vertical_order_traversal_of_a_binary_tree import TreeNode, Solution


class TestVerticalOrderTraversalOfABinaryTree(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=3)

        root.left = TreeNode(val=9)

        root.right = TreeNode(val=20)
        root.right.left = TreeNode(val=15)
        root.right.right = TreeNode(val=7)

        ans = Solution().verticalTraversal(root=root)
        assert ans == [[9], [3, 15], [20], [7]]

    def test_example_2(self):
        root = TreeNode(val=1)

        root.left = TreeNode(val=2)
        root.left.left = TreeNode(val=4)
        root.left.right = TreeNode(val=5)

        root.right = TreeNode(val=3)
        root.right.left = TreeNode(val=6)
        root.right.right = TreeNode(val=7)

        ans = Solution().verticalTraversal(root=root)
        assert ans == [[4], [2], [1, 5, 6], [3], [7]]

import unittest

from closest_binary_search_tree import TreeNode, Solution


class TestBinarySearchTree(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=4)
        root.left = TreeNode(val=2)
        root.left.left = TreeNode(val=1)
        root.left.right = TreeNode(val=3)
        root.right = TreeNode(val=5)
        assert Solution().closestValue(root=root, target=3.714286) == 4
        assert Solution().closestValue(root=root, target=3.1) == 3

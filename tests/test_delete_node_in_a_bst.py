import unittest

from delete_node_in_a_bst import Solution, TreeNode


class TestDeleteNodeInABST(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(val=5)
        root.left = TreeNode(val=3)
        root.left.left = TreeNode(val=2)
        root.left.right = TreeNode(val=4)
        root.right = TreeNode(val=6)
        root.right.right = TreeNode(val=7)

        node = Solution().deleteNode(root=root, key=3)

        assert node.val == 5
        assert node.left.val == 2
        assert node.left.left is None
        assert node.left.right.val == 4
        assert node.right.val == 6
        assert node.right.left is None
        assert node.right.right.val == 7

    def test_example_2(self):
        root = TreeNode(val=0)

        node = Solution().deleteNode(root=root, key=0)

        assert node is None

    def test_example_3(self):
        root = TreeNode(val=3)
        root.left = TreeNode(val=2)
        root.left.left = TreeNode(val=1)
        root.right = TreeNode(val=4)

        node = Solution().deleteNode(root=root, key=3)

        assert node.val == 2
        assert node.left.val == 1
        assert node.left.left is None
        assert node.left.right is None
        assert node.right.val == 4
        assert node.right.left is None
        assert node.right.right is None

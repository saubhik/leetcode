import unittest

from insert_into_a_binary_search_tree import OfficialSolution, Solution, TreeNode


class TestInsertIntoABinarySearchTree(unittest.TestCase):
    def test_example_1(self):
        for solution in (Solution(), OfficialSolution()):
            root = TreeNode(val=4)

            root.left = TreeNode(val=2)
            root.left.left = TreeNode(val=1)
            root.left.right = TreeNode(val=3)

            root.right = TreeNode(val=7)

            root = solution.insertIntoBST(root=root, val=5)
            assert root.right.left.val == 5

            del root

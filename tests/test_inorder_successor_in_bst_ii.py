import unittest

from inorder_successor_in_bst_ii import Node, Solution, SolutionTwo


class TestInorderSuccessorInBSTII(unittest.TestCase):
    def test_example_1(self):
        root = Node(val=2)
        root.left = Node(val=1)
        root.left.parent = root
        root.right = Node(val=3)
        root.right.parent = root

        assert Solution().inorderSuccessor(node=root.left) == root
        assert SolutionTwo().inorderSuccessor(node=root.left) == root

    def test_example_2(self):
        assert Solution().inorderSuccessor(node=Node(val=0)) is None
        assert SolutionTwo().inorderSuccessor(node=Node(val=0)) is None

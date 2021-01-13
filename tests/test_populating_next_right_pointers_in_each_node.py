from unittest import TestCase

from populating_next_right_pointers_in_each_node import Node, OfficialSolution, Solution


class TestPopulatingNextRightPointersInEachNode(TestCase):
    def test_example_1(self):
        for solution in (Solution(), OfficialSolution()):
            root = Node(val=1)
            root.left = Node(val=2)
            root.left.left = Node(val=4)
            root.left.right = Node(val=5)
            root.right = Node(val=3)
            root.right.left = Node(val=6)
            root.right.right = Node(val=7)

            root = solution.connect(root=root)

            assert root.val == 1 and root.next is None
            assert root.left.val == 2 and root.left.next is root.right
            assert root.right.val == 3 and root.right.next is None
            assert root.left.left.val == 4 and root.left.left.next == root.left.right
            assert root.left.right.val == 5 and root.left.right.next == root.right.left
            assert root.right.left.val == 6 and root.right.left.next == root.right.right
            assert root.right.right.val == 7 and root.right.right.next is None

import unittest

from clone_n_ary_tree import Solution, Node


class TestCloneNAryTree(unittest.TestCase):
    def test_example_1(self):
        root = Node(val=1)
        root.children = [Node(val=3), Node(val=2), Node(val=4)]
        root.children[0].children = [Node(val=5), Node(val=6)]

        clone = Solution().cloneTree(root=root)

        assert clone.val == 1
        assert len(clone.children) == 3

        assert clone.children[0].val == 3
        assert len(clone.children[0].children) == 2
        assert clone.children[0].children[0].val == 5
        assert clone.children[0].children[1].val == 6

        assert clone.children[1].val == 2
        assert len(clone.children[1].children) == 0

        assert clone.children[2].val == 4
        assert len(clone.children[2].children) == 0

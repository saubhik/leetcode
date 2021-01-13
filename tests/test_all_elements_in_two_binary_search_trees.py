import unittest

from all_elements_in_two_binary_search_trees import Solution, SolutionTwo, TreeNode


class TestAllElementsInTwoBinarySearchTrees(unittest.TestCase):
    def test_example_1(self):
        #  2
        # 1 4
        root1 = TreeNode(val=2)
        root1.left = TreeNode(val=1)
        root1.right = TreeNode(val=4)

        #  1
        # 0 3
        root2 = TreeNode(val=1)
        root2.left = TreeNode(val=0)
        root2.right = TreeNode(val=3)

        assert Solution().getAllElements(root1=root1, root2=root2) == [
            0,
            1,
            1,
            2,
            3,
            4,
        ]
        assert SolutionTwo().getAllElements(root1=root1, root2=root2) == [
            0,
            1,
            1,
            2,
            3,
            4,
        ]

    def test_example_2(self):
        assert Solution().getAllElements(root1=None, root2=None) == []
        assert SolutionTwo().getAllElements(root1=None, root2=None) == []

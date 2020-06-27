import unittest

from n_ary_tree_level_order_traversal import Solution, Node


class TestLevelOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.solve = Solution().levelOrder

    def test_example_1(self):
        node1 = Node(val=1, children=[])
        node3 = Node(val=3, children=[])
        node2 = Node(val=2, children=[])
        node4 = Node(val=4, children=[])
        node5 = Node(val=5, children=[])
        node6 = Node(val=6, children=[])
        node1.children = [node3, node2, node4]
        node3.children = [node5, node6]

        self.assertListEqual(
            list1=self.solve(root=node1), list2=[[1], [3, 2, 4], [5, 6]]
        )

    def test_example_2(self):
        nodes = list()
        for i in range(1, 15):
            nodes.append(Node(val=i, children=list()))

        nodes[0].children = [nodes[1], nodes[2], nodes[3], nodes[4]]
        nodes[2].children = [nodes[5], nodes[6]]
        nodes[3].children = [nodes[7]]
        nodes[4].children = [nodes[8], nodes[9]]
        nodes[6].children = [nodes[10]]
        nodes[7].children = [nodes[11]]
        nodes[8].children = [nodes[12]]
        nodes[10].children = [nodes[13]]

        for node in nodes:
            print(node.val)

        self.assertListEqual(
            list1=self.solve(root=nodes[0]),
            list2=[[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]],
        )

    def test_empty_input(self):
        self.assertListEqual(list1=self.solve(root=None), list2=[])

import unittest

from reorder_list import ListNode, Solution


class TestReorderList(unittest.TestCase):
    def test_example_1(self):
        node_1 = ListNode(val=1)
        node_2 = ListNode(val=2)
        node_3 = ListNode(val=3)
        node_4 = ListNode(val=4)

        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4

        Solution().reorderList(head=node_1)

        assert node_1.next == node_4
        assert node_4.next == node_2
        assert node_2.next == node_3

    def test_example_2(self):
        node_1 = ListNode(val=1)
        node_2 = ListNode(val=2)
        node_3 = ListNode(val=3)
        node_4 = ListNode(val=4)
        node_5 = ListNode(val=5)

        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5

        Solution().reorderList(head=node_1)

        assert node_1.next == node_5
        assert node_5.next == node_2
        assert node_2.next == node_4
        assert node_4.next == node_3

    def test_example_3(self):
        assert Solution().reorderList(head=None) is None

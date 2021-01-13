import unittest

from insert_into_a_sorted_circular_linked_list import Node, Solution


class TestInsertIntoASortedCircularLinkedList(unittest.TestCase):
    def test_example_1(self):
        head = Node(val=1)
        head.next = Node(val=3)
        head.next.next = Node(val=4)
        head.next.next.next = head
        node = Solution().insert(head=head, insertVal=2)
        assert node.val == 1
        assert node.next.val == 2
        assert node.next.next.val == 3
        assert node.next.next.next.val == 4
        assert node.next.next.next.next == node

    def test_example_2(self):
        node = Solution().insert(head=None, insertVal=2)
        assert node.val == 2
        assert node.next == node

    def test_example_3(self):
        head = Node(val=1)
        head.next = head
        node = Solution().insert(head=head, insertVal=2)
        assert node.val == 1
        assert node.next.val == 2
        assert node.next.next == node

import unittest

from convert_binary_number_in_a_linked_list_to_integer import ListNode, Solution


class TestBinaryNumberInALinkedListToInteger(unittest.TestCase):
    def test_example_1(self):
        head = ListNode(val=1)
        head.next = ListNode(val=0)
        head.next.next = ListNode(val=1)

        assert Solution().getDecimalValue(head=head) == 5

    def test_example_2(self):
        head = ListNode(val=0)

        assert Solution().getDecimalValue(head=head) == 0

    def test_example_3(self):
        head = ListNode(val=1)

        assert Solution().getDecimalValue(head=head) == 1

    def test_example_4(self):
        vals = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        node = sentinel = ListNode(val=-1)
        for val in vals:
            node.next = ListNode(val=val)
            node = node.next

        assert Solution().getDecimalValue(head=sentinel.next) == 18880

    def test_example_5(self):
        head = ListNode(val=0)
        head.next = ListNode(val=0)

        assert Solution().getDecimalValue(head=head) == 0

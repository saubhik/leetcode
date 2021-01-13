from typing import List
from unittest import TestCase

from merge_in_between_linked_lists import ListNode, Solution


class TestMergeInBetweenLinkedLists(TestCase):
    def _create_linked_list(self, values: List[int]) -> ListNode:
        curr = lis = ListNode()
        for val in values:
            curr.next = ListNode(val=val)
            curr = curr.next
        return lis.next

    def _get_values_from_list(self, list: ListNode) -> List[int]:
        values = []
        while list:
            values.append(list.val)
            list = list.next
        return values

    def test_example_1(self):
        assert (
            self._get_values_from_list(
                Solution().mergeInBetween(
                    list1=self._create_linked_list(values=[0, 1, 2, 3, 4, 5]),
                    a=3,
                    b=4,
                    list2=self._create_linked_list(values=[1000000, 1000001, 1000002]),
                )
            )
            == [0, 1, 2, 1000000, 1000001, 1000002, 5]
        )

    def test_example_2(self):
        assert (
            self._get_values_from_list(
                Solution().mergeInBetween(
                    list1=self._create_linked_list(values=[0, 1, 2, 3, 4, 5, 6]),
                    a=2,
                    b=5,
                    list2=self._create_linked_list(
                        values=[1000000, 1000001, 1000002, 1000003, 1000004]
                    ),
                )
            )
            == [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
        )

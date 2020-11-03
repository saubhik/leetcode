# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(n**2)
    # Space Complexity: O(1)
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        sorted_tail = sorted_head = head
        current = head.next
        while current:
            next_current = current.next

            # Remove current from the list.
            sorted_tail.next = next_current

            # Find the correct position to place current.
            greater, lesser = sorted_head, None
            while greater and greater.val < current.val:
                lesser, greater = greater, greater.next

            if not lesser:
                # If current is the least element so far.
                sorted_head = current
            else:
                # Otherwise.
                lesser.next = current

            current.next = greater

            # Extend the sorted_tail if current was appended.
            if sorted_tail.next == current:
                sorted_tail = sorted_tail.next

            current = next_current

        return sorted_head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(n1 + n2).
    # Space Complexity: O(n1 + n2).
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        stack2 = []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        node, carry = None, 0
        while stack1 or stack2 or carry:
            num1 = 0
            if stack1:
                num1 = stack1.pop()

            num2 = 0
            if stack2:
                num2 = stack2.pop()

            result = carry + num1 + num2
            carry, val = result // 10, result % 10
            node = ListNode(val=val, next=node)

        return node


class OfficialSolution:
    def get_length(self, node: ListNode) -> int:
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # Time Complexity: O(n1 + n2).
    # Space Complexity: O(1).
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = self.get_length(node=l1), self.get_length(node=l2)

        # Does l1 point to the first node now? Yes.
        node = None
        while n1 or n2:
            num1 = 0
            if n1 >= n2:
                num1 = l1.val
                l1 = l1.next
                n1 -= 1

            num2 = 0
            if n2 > n1:
                num2 = l2.val
                l2 = l2.next
                n2 -= 1

            # Don't care about carry for now.
            node = ListNode(val=num1 + num2, next=node)

        # Reverse the list & care about the carry.
        #         7 -> 2 -> 4  -> 3 -> None
        #              5 -> 6  -> 4 -> None
        # None <- 7 <- 7 <- 10 <- 7
        head, carry = None, 0
        while node:
            remaining = node.val + carry
            new_val, carry = remaining % 10, remaining // 10
            node.val = new_val

            head, node.next, node = node, head, node.next

        if carry:
            head = ListNode(val=carry, next=head)

        return head

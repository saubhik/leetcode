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

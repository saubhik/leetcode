# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.


class Solution:
    # Time: O(N)
    # Space: O(N)
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        values = []

        while True:
            if head is None:
                break

            values.append(head)
            head = head.getNext()

        while values:
            values.pop().printValue()


class SolutionTwo:
    # Without using any data structures.
    # Time: O(N)
    # Space: O(N), implicit recursion call stack.
    def printLinkedListInReverse(self, head) -> None:
        def rec(node):
            if node is None:
                return
            rec(node=node.getNext())
            node.printValue()

        rec(node=head)


class SolutionThree:
    # DivideAndConquer
    # Time: O(NlgN)
    # Space: O(NlgN)
    def printLinkedListInReverse(self, head) -> None:
        def getSize(head):
            size = 0
            while head:
                head = head.getNext()
                size += 1
            return size

        # T(n) = 2 * T(n/2) + n
        # for both space and time.
        def helper(head, n):
            if n >= 2:
                half = head
                for _ in range(n // 2):
                    half = half.getNext()
                helper(half, n - n // 2)
                helper(head, n // 2)
            elif n == 1:
                head.printValue()

        helper(head, n=getSize(head))


class SolutionFour:
    # Space optimised
    # Time: O(N^2)
    # Space: O(1)
    def printLinkedListInReverse(self, head) -> None:
        tail = None
        while tail != head:
            curr = head
            while curr.getNext() != tail:
                curr = curr.getNext()
            tail = curr
            tail.printValue()

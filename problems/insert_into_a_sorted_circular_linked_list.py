# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    # These are the cases:
    # 1. No nodes. (insert head)
    # 2. At least two different nodes.
    #       - curr.val <= insertVal <= curr.next.val (insert to curr.next)
    #       - curr.val > curr.next.val (insert to curr.next)
    # 3. All nodes same. (insert to head.next)
    #
    # Time Complexity: O(n), Two Pass.
    # Space Complexity: O(1).
    def insert(self, head: "Node", insertVal: int) -> "Node":
        if head is None:
            head = Node(val=insertVal)
            head.next = head
            return head

        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                curr.next = Node(val=insertVal, next=curr.next)
                return head
            curr = curr.next
            if curr == head:
                break

        curr = head
        while True:
            if curr.val > curr.next.val:
                curr.next = Node(val=insertVal, next=curr.next)
                return head
            curr = curr.next
            if curr == head:
                break

        head.next = Node(val=insertVal, next=head.next)
        return head


class OfficialSolution:
    def insert(self, head: Node, insertVal: int) -> Node:
        """
        == Approach 1: Two-Pointers Iteration ==

        == Intuition ==
        As simple as the problem might seem to be, it is actually not trivial to write
        a solution that covers all cases.
        Often the case for the problems with linked list, one could apply the approach
        of Two-Pointers Iteration, where one uses two pointers as surrogate to traverse
        the linked list.
        One of the reasons of having two pointers rather than one is that in singly
        linked list one does not have a reference to the precedent node, therefore we
        keep an additional pointer which points to the precedent node.
        For this problem, we iterate through the cyclic list using two pointers, namely
        prev and curr. When we find a suitable place to insert the new value, we insert
        it between the prev and curr nodes.

        == Algorithm ==
        First of all, let us define the skeleton of two pointers iteration algorithm as
        follows:
            - As we mentioned in the intuition, we loop over the linked list with two
            pointers (i.e. prev and curr) step by step. The termination condition of
            the loop is that we get back to the starting point of the two pointers.
            (i.e. prev == head).
            - During the loop, at each step, we check if the current place bounded by
            the two pointers is the right place to insert the new value.
            - If not, we move both pointers one step forwards.

        Now the tricky part of this problem is to sort out different cases that our
        algorithm should deal with within the loop, and then design a concise logic to
        handle them sound and properly. Here we break it down into three general cases.

        Case 1. The value of new node sits between the minimal and maximal values of
        the current list. As a result, it should be inserted within the list.
        The condition is to find the place that meets the constraint of:
        prev.val <= insertVal <= curr.val.

        Case 2. The value of new node goes beyond the minimal and maximal values of the
        current list, either less than the minimal value or greater than the maximal
        value. In either case, the new node should be added right after the tail node (
        i.e. the node with the maximal value of the list).
        Firstly, we should locate the position of the tail node, by finding a descending
        order between the adjacent, i.e. the condition of prev.val > curr.val, since the
        nodes are sorted in ascending order, the tail node would have the greatest value
        of all nodes.

        Case 3. Finally, there is one case that does not fall into any of the above two
        cases. This is the case where the list contains uniform values.
        Though not explicitly stated in the problem description, our sorted list can
        contain some duplicate values. And in the extreme case, the entire list has only
        one single unique value.

        The above three cases cover the scenarios within and after our iteration loop.
        There is however one minor corner case we still need to deal with, where we have
        an empty list. This, we could easily handle before the loop.

        == Complexity Analysis ==
        - Time Complexity: O(n), where N is the size of the list. In the worst case, we
            would iterate through the entire list.
        - Space Complexity: O(1). It is a constant space solution.

        == Own Comments ==
        It is exactly similar to my solution, with
            insertVal >= prev.val or insertVal <= curr.val
        making it a one pass solution.
        """
        if head is None:
            newNode = Node(val=insertVal, next=None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        toInsert = False

        while True:
            if prev.val <= insertVal <= curr.val:
                # Case #1
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. Where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(val=insertVal, next=curr)
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break

        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(val=insertVal, next=curr)
        return head

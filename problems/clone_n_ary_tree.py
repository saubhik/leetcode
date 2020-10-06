# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    """
    Time Complexity: O(n) = O(1) since total number of nodes <= 10_000.
    Space Complexity: O(h) = O(1) since depth of the n-ary tree <= 1000.
    """

    def cloneTree(
        self, root: Optional["Node"] = None, clone: Optional["Node"] = None
    ) -> Optional["Node"]:
        if root is None:
            return None

        if clone is None:
            clone = Node(val=root.val)

        for child in root.children:
            clone.children.append(Node(val=child.val))
            self.cloneTree(root=child, clone=clone.children[-1])

        return clone

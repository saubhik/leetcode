# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        parent = None
        node = root
        while node:
            if key < node.val:
                parent = node
                node = parent.left
            elif key > node.val:
                parent = node
                node = parent.right
            else:
                break

        if node is None:
            return root

        # get the right most leaf of left subtree, if exists
        # else get the left most leaf of right subtree, if exists
        # else just delete
        if node.left:
            parent = None
            nl = node.left
            while nl.right:
                parent = nl
                nl = parent.right

            node.val = nl.val
            if parent is not None:
                parent.right = nl.left
            else:
                node.left = nl.left
        elif node.right:
            parent = None
            nr = node.right
            while nr.left:
                parent = nr
                nr = parent.left

            node.val = nr.val
            if parent is not None:
                parent.left = nr.right
            else:
                node.right = nr.right
        else:
            # node is a leaf
            if parent and parent.left == node:
                parent.left = None
            elif parent and parent.right == node:
                parent.right = None
            else:
                root = None

        return root

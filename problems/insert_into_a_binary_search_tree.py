# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Straight Forward DFS.
    Time Complexity: O(h) = O(n) in worst case.
    Space Complexity: O(h) = O(n) in worst case (recursion call stack).
        Here, h is the height of the tree, and n is the number of nodes.
    """

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val=val)

        if val < root.val:
            root.left = self.insertIntoBST(root=root.left, val=val)
        elif val > root.val:
            root.right = self.insertIntoBST(root=root.right, val=val)

        return root


class OfficialSolution:
    """
    Iterative Constant Space solution.
    Time Complexity: O(h) = O(n) in worst case.
    Space Complexity: O(1).
    """

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val=val)

        node = root
        while True:
            if node.val < val:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = TreeNode(val=val)
                    return root
            elif node.val > val:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = TreeNode(val=val)
                    return root

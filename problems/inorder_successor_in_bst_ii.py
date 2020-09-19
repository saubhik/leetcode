# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    # Straight Forward In-Order DFS.
    #
    # Time: O(n) time, where n is the number of nodes.
    # Space: O(n) additional space, due to recursion call stack in worst case.
    #
    # Consider the tree:
    #       4
    #   2      6
    # 1  3   5  7
    # If node = Node(5,...), then return Node(6,...).
    #
    def inorderSuccessor(self, node: "Node") -> "Node":
        # search for the root
        root = node
        while root.parent:
            root = root.parent

        found = False

        def inorder_dfs(curr_node: "Node") -> "Node":
            nonlocal found

            if not curr_node:
                return None

            found_node_left = inorder_dfs(curr_node=curr_node.left)
            if found_node_left is not None:
                return found_node_left

            if found:
                return curr_node

            if curr_node == node:
                found = True

            found_node_right = inorder_dfs(curr_node=curr_node.right)
            if found_node_right is not None:
                return found_node_right

        return inorder_dfs(curr_node=root)


class SolutionTwo:
    # There is O(1) space solution.
    # Time: O(H) i.e. O(lgN) in average case, and O(N) in worst case.
    # Space: O(1)
    #
    # Case wise:
    # 1. Node has right subtree.
    #    In this case, keep going left. The left-most node (leaf or without right
    #    subtree is the successor).
    # 2. Node has no right subtree.
    #    In this case, successor is up in the tree or None.
    #    Keep going up along the right branches, until we encounter a left branch.
    #    The parent of the left branch is the successor.
    def inorderSuccessor(self, node: Node):
        if node.right is not None:
            node = node.right
            while node.left:
                node = node.left
            return node

        # case when node has no right subtree
        # move up along right branches
        while node.parent and node.parent.right == node:
            node = node.parent
        # either None or curr.parent.left == curr
        return node.parent

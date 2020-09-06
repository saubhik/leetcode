from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(m+n)
    # Space: O(m+n)
    # This is one-pass solution.
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        ans, stack1, stack2 = [], [], []

        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left

            while root2:
                stack2.append(root2)
                root2 = root2.left

            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                root1 = stack1.pop()
                ans.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                ans.append(root2.val)
                root2 = root2.right

        return ans


class SolutionTwo:
    # Do in-order traversal of BST to get the node values in sorted order for each
    # BST. Then merge them as in MergeSort.
    # Time: O(n+m).
    # Space: O(n+m).
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node: Optional[TreeNode], ans: Optional[List[int]] = None):
            if ans is None:
                ans = []

            if node is None:
                return []

            if node.left is not None:
                dfs(node=node.left, ans=ans)

            ans.append(node.val)

            if node.right is not None:
                dfs(node=node.right, ans=ans)

            return ans

        left = dfs(node=root1)
        right = dfs(node=root2)

        n_left = len(left)
        n_right = len(right)

        i, j = 0, 0
        ans = []
        while i < n_left and j < n_right:
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        for i in range(i, n_left):
            ans.append(left[i])

        for j in range(j, n_right):
            ans.append(right[j])

        return ans

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # Straight Forward BFS.
        if root is None:
            return ""

        ans, level = "", list()
        level.append(root)
        while level:
            new_level = []
            for node in level:
                ans += str(node.val) if ans == "" else f",{node.val}"
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level

        return ans

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        root = None
        if data == "":
            return root

        def insert_to_BST(root: TreeNode, value: int) -> TreeNode:
            if root is None:
                return TreeNode(value)

            node = root
            while True:
                if value < node.val:
                    if node.left is None:
                        node.left = TreeNode(value)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = TreeNode(value)
                        break
                    node = node.right

            return root

        values = map(int, data.split(","))
        for value in values:
            root = insert_to_BST(root=root, value=value)

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


class OfficialSolution:
    """
    == How to make the encoded string as compact as possible ==
    To serialize a binary tree means to:
    - Encode tree structure.
    - Encode node values.
    - Choose delimiters to separate the values in the encoded string.
    """

    class CodecApproach1:
        """
        == Approach 1 ==
        Post Order Traversal to optimise space for the tree structure.
        == Intuition ==
        Let's use here the fact that BST could be constructed from preorder or postorder
        traversal only. In brief, it's a consequence of 2 facts:
            1. Binary tree could be constructed from preorder/postorder and inorder
            traversal.
            2. Inorder traversal of BST is an array sorted in the ascending order. We have,
            inorder = sorted(preorder).
        This means that BST structure is already encoded in the preorder or postorder
        traversal and hence they are both suitable for the compact serialization.
        Serialization could be easily implemented with both strategies, but for optimal
        deserialization better to choose the postorder traversal because member/global/
        static variables are not allowed here.

        == Complexity Analysis ==
        - Time Complexity: O(N) both for serialization and deserialization.
        - Space Complexity: O(N) since we store the entire tree. Encoded string: one needs
            to store (N-1) delimiters, and N node values in the encoded string. Tree
            structure is encoded in the order of values and uses no space.
        """

        def serialize(self, root: TreeNode):
            def postorder(node: TreeNode):
                # Space: O(n) + O(lgn) recursion stack = O(n)
                # Time: O(n)
                return (
                    (
                        postorder(node=node.left)
                        + postorder(node=node.right)
                        + [node.val]
                    )
                    if node
                    else []
                )

            return ",".join(map(str, postorder(node=root)))

        def deserialize(self, data: str) -> Optional[TreeNode]:
            #    5
            #   3  9
            #  1 4   10
            # Postorder traversal is: "1,4,3,10,9,5"
            def helper(upper: float = float("inf"), lower: float = float("-inf")):
                if not data or data[-1] < lower or data[-1] > upper:
                    return None

                val = data.pop()
                node = TreeNode(val)
                node.right = helper(lower=val, upper=upper)
                node.left = helper(upper=val, lower=lower)
                return node

            data = list(map(int, data.split(",")))
            return helper()

    class CodecApproach2:
        """
        == Approach 2 ==
        Convert int to 4 bytes string to optimise space for node values.
        Approach 1 works fine with small node values but starts to consume more and more
        space in the case of large ones.
        For example, the tree [2,null,3,null,4] is encoded as a string "4,3,2" which
        uses 5 bytes to store the values and delimiters, 1 byte per value or delimiter.
        So far everything is fine.
        Let's consider now the tree [12345,null,12346,null,12347] which is encoded as
        "12347,12346,12345" and consumes 17 bytes to store 3 integers and 2 delimiters,
        15 bytes for node values only. At the same time it's known that 4 bytes is
        enough to store an int value, i.e. 12 bytes should be enough for 3 integers
        and hence the storage of values could be optimised.

        == Complexity Analysis ==
        Time Complexity: O(N) both for serialization and deserialization.
        Space Complexity: O(N), since we store the entire tree.
            Encoded string: one needs 2*(N-1) bytes for the delimiters (delimiter
                cannot fit in 1 byte, since it might collide with a byte from a node
                value), and 4*N bytes for the node values in the encoded string. Tree
                structure is encoded in the order of node values and uses no space.
        """

        def postorder(self, root: Optional[TreeNode]) -> List[int]:
            return (
                (
                    self.postorder(root=root.left)
                    + self.postorder(root=root.right)
                    + [root.val]
                )
                if root
                else []
            )

        def int_to_str(self, x: int) -> str:
            # 0xFF = 0b11111111.
            # x >> 0 & 0xFF are last 8 bits.
            # x >> 8 & 0xFF are the next 8 bits from the last.
            # x >> 16 & 0xFF are the next 8 bits.
            # x >> 24 & 0xFF are the next 8 bits.
            bytes = [chr(x >> (i * 8) & 0xFF) for i in range(4)]
            bytes.reverse()
            bytes_str = "".join(bytes)
            return bytes_str

        def serialize(self, root: Optional[TreeNode]) -> str:
            return chr(256).join(map(self.int_to_str, self.postorder(root=root)))

        def str_to_int(self, bytes_str: str) -> int:
            ans = 0
            for ch in bytes_str:
                ans = ans * 256 + ord(ch)
            return ans

        def deserialize(self, data: str) -> Optional[TreeNode]:
            def helper(upper=float("inf"), lower=float("-inf")) -> Optional[TreeNode]:
                if not data or data[-1] < lower or data[-1] > upper:
                    return None
                val = data.pop()
                node = TreeNode(val)
                node.right = helper(lower=val, upper=upper)
                node.left = helper(upper=val, lower=lower)
                return node

            data = list(map(self.str_to_int, data.split(chr(256))))
            return helper()

    class CodecApproach3(CodecApproach2):
        """
        == Approach 3 ==
        Get rid of delimiters.
        == Intuition ==
        Approach 2 works well except for delimiter usage.
        Since all node values are now encoded as 4-bytes strings, one could just split
        the encoded string into 4-bytes chunks, convert each chunk back to the integer
        and proceed further.

        So, we have:
            1. 12 bytes for node values
            2. 0 bytes for delimiters
            3. 0 bytes for tree structure

        == Complexity Analysis ==
        Time Complexity: O(N) both for serialization and deserialization.
        Space Complexity: O(N), since we store the entire tree.
            Encoded string: no delimiters, no additional space for the tree structure,
            just 4N bytes for the node values in the encoded string.
        """

        def serialize(self, root: Optional[TreeNode]) -> str:
            return "".join(map(self.int_to_str, self.postorder(root=root)))

        def deserialize(self, data: str) -> Optional[TreeNode]:
            def helper(lower=float("-inf"), upper=float("inf")) -> Optional[TreeNode]:
                if not data or data[-1] < lower or data[-1] > upper:
                    return None
                val = data.pop()
                node = TreeNode(val)
                node.right = helper(lower=val, upper=upper)
                node.left = helper(lower=lower, upper=val)
                return node

            data = [
                self.str_to_int(bytes_str=data[4 * i : 4 * i + 4])
                for i in range(0, len(data) // 4)
            ]

            return helper()

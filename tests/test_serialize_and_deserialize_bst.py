import unittest

from serialize_and_deserialize_bst import TreeNode, Codec, OfficialSolution


class TestSerializeAndDeserializeBST(unittest.TestCase):
    def test_example_1(self):
        for CodecClass in (
            Codec,
            OfficialSolution().CodecApproach1,
            OfficialSolution().CodecApproach2,
            OfficialSolution.CodecApproach3,
        ):
            root = TreeNode(x=2)
            root.left = TreeNode(x=1)
            root.right = TreeNode(x=3)

            ser, deser = CodecClass(), CodecClass()
            tree = ser.serialize(root=root)
            node = deser.deserialize(data=tree)

            assert node.val == 2
            assert node.left.val == 1
            assert node.left.left is None
            assert node.left.right is None
            assert node.right.val == 3
            assert node.right.left is None
            assert node.right.right is None

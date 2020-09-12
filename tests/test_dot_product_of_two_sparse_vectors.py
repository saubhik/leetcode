import unittest

from dot_product_of_two_sparse_vectors import SparseVector


class TestDotProductOfTwoSparseVectors(unittest.TestCase):
    def test_example_1(self):
        v1 = SparseVector(nums=[1, 0, 0, 2, 3])
        v2 = SparseVector(nums=[0, 3, 0, 4, 0])
        assert v1.dotProduct(vec=v2) == 8

    def test_example_2(self):
        v1 = SparseVector(nums=[0, 1, 0, 0, 0])
        v2 = SparseVector(nums=[0, 0, 0, 0, 2])
        assert v1.dotProduct(vec=v2) == 0

    def test_example_3(self):
        v1 = SparseVector(nums=[0, 1, 0, 0, 2, 0, 0])
        v2 = SparseVector(nums=[1, 0, 0, 0, 3, 0, 4])
        assert v1.dotProduct(vec=v2) == 6

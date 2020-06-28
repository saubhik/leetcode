import unittest

from top_k_frequent_elements import Solution


class TestTopKFrequent(unittest.TestCase):
    def setUp(self) -> None:
        self.solve = Solution().topKFrequent
        self.solve2 = Solution().topKFrequent2

    def test_example_1(self):
        assert set(self.solve(nums=[1, 1, 1, 2, 2, 3], k=2)) == {1, 2}
        assert set(self.solve2(nums=[1, 1, 1, 2, 2, 3], k=2)) == {1, 2}

    def test_example_2(self):
        assert set(self.solve(nums=[1], k=1)) == {1}
        assert set(self.solve2(nums=[1], k=1)) == {1}

    def test_example_3(self):
        assert set(self.solve(nums=[4, 1, -1, 2, -1, 2, 3], k=2)) == {-1, 2}
        assert set(self.solve2(nums=[4, 1, -1, 2, -1, 2, 3], k=2)) == {-1, 2}

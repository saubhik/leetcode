import unittest

from contains_duplicate_iii import Solution, SolutionTwo


class TestContainsNearbyAlmostDuplicate(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0)
            is True
        )
        assert (
            SolutionTwo().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0)
            is True
        )

    def test_example_2(self):
        assert (
            Solution().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2)
            is True
        )
        assert (
            SolutionTwo().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2)
            is True
        )

    def test_example_3(self):
        assert (
            Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3)
            is False
        )
        assert (
            SolutionTwo().containsNearbyAlmostDuplicate(
                nums=[1, 5, 9, 1, 5, 9], k=2, t=3
            )
            is False
        )

    def test_example_4(self):
        assert (
            SolutionTwo().containsNearbyAlmostDuplicate(nums=[-1, -1], k=1, t=-1)
            is False
        )

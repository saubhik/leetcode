from unittest import TestCase

from the_kth_factor_of_n import Solution, SolutionTwo, SolutionThree


class TestTheKthFactorOfN(TestCase):
    def test_example_1(self):
        assert Solution().kthFactor(n=12, k=3) == 3
        assert SolutionTwo().kthFactor(n=12, k=3) == 3
        assert SolutionThree().kthFactor(n=12, k=3) == 3

    def test_example_2(self):
        assert Solution().kthFactor(n=7, k=2) == 7
        assert SolutionTwo().kthFactor(n=7, k=2) == 7
        assert SolutionThree().kthFactor(n=7, k=2) == 7

    def test_example_3(self):
        assert Solution().kthFactor(n=4, k=4) == -1
        assert SolutionTwo().kthFactor(n=4, k=4) == -1
        assert SolutionThree().kthFactor(n=4, k=4) == -1

    def test_example_4(self):
        assert Solution().kthFactor(n=1, k=1) == 1
        assert SolutionTwo().kthFactor(n=1, k=1) == 1
        assert SolutionThree().kthFactor(n=1, k=1) == 1

    def test_example_5(self):
        assert Solution().kthFactor(n=1000, k=3) == 4
        assert SolutionTwo().kthFactor(n=1000, k=3) == 4
        assert SolutionThree().kthFactor(n=1000, k=3) == 4

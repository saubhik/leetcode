import unittest

from power_of_four import Solution, SolutionFour, SolutionThree, SolutionTwo


class TestPowerOfFour(unittest.TestCase):
    def test_example(self):
        assert Solution().isPowerOfFour(num=16) is True
        assert Solution().isPowerOfFour(num=5) is False
        assert Solution().isPowerOfFour(num=0) is False
        assert Solution().isPowerOfFour(num=1) is True
        assert Solution().isPowerOfFour(num=1162261466) is False

    def test_example_two(self):
        assert SolutionTwo().isPowerOfFour(num=16) is True
        assert SolutionTwo().isPowerOfFour(num=5) is False
        assert SolutionTwo().isPowerOfFour(num=0) is False
        assert SolutionTwo().isPowerOfFour(num=1) is True
        assert SolutionTwo().isPowerOfFour(num=1162261466) is False

    def test_example_three(self):
        assert SolutionThree().isPowerOfFour(num=16) is True
        assert SolutionThree().isPowerOfFour(num=5) is False
        assert SolutionThree().isPowerOfFour(num=0) is False
        assert SolutionThree().isPowerOfFour(num=1) is True
        assert SolutionThree().isPowerOfFour(num=1162261466) is False

    def test_example_four(self):
        assert SolutionFour().isPowerOfFour(num=16) is True
        assert SolutionFour().isPowerOfFour(num=5) is False
        assert SolutionFour().isPowerOfFour(num=0) is False
        assert SolutionFour().isPowerOfFour(num=1) is True
        assert SolutionFour().isPowerOfFour(num=1162261466) is False

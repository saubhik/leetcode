from unittest import TestCase

from concatenation_of_consecutive_binary_numbers import Solution, SolutionTwo


class TestConcatenationOfConsecutiveBinaryNumbers(TestCase):
    def test_example_1(self):
        assert Solution().concatenatedBinary(n=1) == 1
        assert SolutionTwo().concatenatedBinary(n=1) == 1

    def test_example_2(self):
        assert Solution().concatenatedBinary(n=3) == 27
        assert SolutionTwo().concatenatedBinary(n=3) == 27

    def test_example_3(self):
        assert Solution().concatenatedBinary(n=12) == 505379714
        assert SolutionTwo().concatenatedBinary(n=12) == 505379714

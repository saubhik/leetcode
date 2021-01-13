import unittest

from sequential_digits import Solution, SolutionThree, SolutionTwo


class TestSequentialDigits(unittest.TestCase):
    def test_example_1(self):
        assert Solution().sequentialDigits(low=100, high=300) == [123, 234]
        assert SolutionTwo().sequentialDigits(low=100, high=300) == [123, 234]
        assert SolutionThree().sequentialDigits(low=100, high=300) == [123, 234]

    def test_example_2(self):
        assert Solution().sequentialDigits(low=1000, high=13000) == [
            1234,
            2345,
            3456,
            4567,
            5678,
            6789,
            12345,
        ]
        assert SolutionTwo().sequentialDigits(low=1000, high=13000) == [
            1234,
            2345,
            3456,
            4567,
            5678,
            6789,
            12345,
        ]
        assert SolutionThree().sequentialDigits(low=1000, high=13000) == [
            1234,
            2345,
            3456,
            4567,
            5678,
            6789,
            12345,
        ]

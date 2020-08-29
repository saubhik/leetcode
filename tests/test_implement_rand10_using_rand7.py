import unittest

from implement_rand10_using_rand7 import Solution, SolutionTwo


class TestImplementRand10UsingRand7(unittest.TestCase):
    def test_example_1(self):
        assert set([Solution().rand10() for _ in range(1000)]) == {
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
        }
        assert set([SolutionTwo().rand10() for _ in range(1000)]) == {
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
        }

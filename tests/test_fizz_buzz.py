import unittest

from fizz_buzz import Solution


class TestFizzBuzz(unittest.TestCase):
    def test_example_1(self):
        assert Solution().fizzBuzz(n=15) == [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]

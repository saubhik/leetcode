from unittest import TestCase

from numbers_at_most_n_given_digit_set import Solution


class TestNumbersAtMostNGivenDigitSet(TestCase):
    def test_example_1(self):
        assert Solution().atMostNGivenDigitSet(digits=["1", "3", "5", "7"], n=100) == 20

    def test_example_2(self):
        assert (
            Solution().atMostNGivenDigitSet(digits=["1", "4", "9"], n=1000000000)
            == 29523
        )

    def test_example_3(self):
        assert Solution().atMostNGivenDigitSet(digits=["7"], n=8) == 1

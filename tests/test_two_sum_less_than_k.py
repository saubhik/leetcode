from unittest import TestCase

from two_sum_less_than_k import Solution


class TestTwoSumLessThanK(TestCase):
    def test_example_1(self):
        assert Solution().twoSumLessThanK(A=[34, 23, 1, 24, 75, 33, 54, 8], K=60) == 58

    def test_example_2(self):
        assert Solution().twoSumLessThanK(A=[10, 20, 30], K=15) == -1

    def test_example_3(self):
        assert (
            Solution().twoSumLessThanK(
                A=[
                    254,
                    914,
                    110,
                    900,
                    147,
                    441,
                    209,
                    122,
                    571,
                    942,
                    136,
                    350,
                    160,
                    127,
                    178,
                    839,
                    201,
                    386,
                    462,
                    45,
                    735,
                    467,
                    153,
                    415,
                    875,
                    282,
                    204,
                    534,
                    639,
                    994,
                    284,
                    320,
                    865,
                    468,
                    1,
                    838,
                    275,
                    370,
                    295,
                    574,
                    309,
                    268,
                    415,
                    385,
                    786,
                    62,
                    359,
                    78,
                    854,
                    944,
                ],
                K=200,
            )
            == 198
        )

import unittest

from complement_of_base_10_integer import Solution, OfficialSolution


class TestComplementOfBase10Integer(unittest.TestCase):
    def test_example_1(self):
        assert Solution().bitwiseComplement(N=5) == 2
        assert OfficialSolution().bitwiseComplement(N=5) == 2

    def test_example_2(self):
        assert Solution().bitwiseComplement(N=7) == 0
        assert OfficialSolution().bitwiseComplement(N=7) == 0

    def test_example_3(self):
        assert Solution().bitwiseComplement(N=10) == 5
        assert OfficialSolution().bitwiseComplement(N=10) == 5

    def test_example_4(self):
        assert Solution().bitwiseComplement(N=0) == 1
        assert OfficialSolution().bitwiseComplement(N=0) == 1

    def test_example_5(self):
        assert Solution().bitwiseComplement(N=1) == 0
        assert OfficialSolution().bitwiseComplement(N=1) == 0

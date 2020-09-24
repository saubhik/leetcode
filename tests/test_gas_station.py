import unittest

from gas_station import Solution, OfficialSolution


class TestGasStation(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
            == 3
        )
        assert (
            OfficialSolution().canCompleteCircuit(
                gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]
            )
            == 3
        )

    def test_example_2(self):
        assert Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
        assert (
            OfficialSolution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
        )

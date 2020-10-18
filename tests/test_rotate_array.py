import unittest

from rotate_array import Solution, OfficialSolutionApproach4


class TestRotateArray(unittest.TestCase):
    def test_example_1(self):
        for solution in (Solution(), OfficialSolutionApproach4()):
            nums = [1, 2, 3, 4, 5, 6, 7]
            solution.rotate(nums=nums, k=3)
            assert nums == [
                5,
                6,
                7,
                1,
                2,
                3,
                4,
            ]

    def test_example_2(self):
        for solution in (Solution(), OfficialSolutionApproach4()):
            nums = [-1, -100, 3, 99]
            solution.rotate(nums=nums, k=2)
            assert nums == [3, 99, -1, -100]

    def test_example_3(self):
        for solution in (Solution(), OfficialSolutionApproach4()):
            nums = [1]
            solution.rotate(nums=nums, k=0)
            assert nums == nums

    def test_example_4(self):
        for solution in (Solution(), OfficialSolutionApproach4()):
            nums = [1]
            solution.rotate(nums=nums, k=1)
            assert nums == nums

    def test_example_5(self):
        for solution in (Solution(), OfficialSolutionApproach4()):
            nums = [1, 2, 3, 4, 5, 6]
            solution.rotate(nums=nums, k=4)
            assert nums == [3, 4, 5, 6, 1, 2]

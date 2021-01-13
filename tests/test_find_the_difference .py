import unittest

from find_the_difference import OfficialSolution, Solution


class TestFindTheDifference(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findTheDifference(s="abcd", t="abcde") == "e"
        assert OfficialSolution().findTheDifferenceApproach3(s="abcd", t="abcde") == "e"

import unittest

from remove_duplicate_letters import OfficialSolution


class TestRemoveDuplicateLetters(unittest.TestCase):
    def test_example_1(self):
        assert OfficialSolution().Approach1().removeDuplicateLetters(s="bcabc") == "abc"
        assert OfficialSolution().Approach2().removeDuplicateLetters(s="bcabc") == "abc"

    def test_example_2(self):
        assert (
            OfficialSolution().Approach1().removeDuplicateLetters(s="cbacdcbc")
            == "acdb"
        )
        assert (
            OfficialSolution().Approach2().removeDuplicateLetters(s="cbacdcbc")
            == "acdb"
        )

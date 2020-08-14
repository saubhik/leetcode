import unittest

from iterator_for_combination import CombinationIterator, CombinationIteratorII


class TestCombinationIterator(unittest.TestCase):
    def test_example_1(self):
        obj = CombinationIterator(characters="abc", combinationLength=2)
        assert obj.next() == "ab"
        assert obj.hasNext() is True
        assert obj.next() == "ac"
        assert obj.hasNext() is True
        assert obj.next() == "bc"
        assert obj.hasNext() is False

    def test_example_2(self):
        obj = CombinationIteratorII(characters="abc", combinationLength=2)
        assert obj.next() == "ab"
        assert obj.hasNext() is True
        assert obj.next() == "ac"
        assert obj.hasNext() is True
        assert obj.next() == "bc"
        assert obj.hasNext() is False

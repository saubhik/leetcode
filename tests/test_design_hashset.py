import unittest

from design_hashset import MyHashSet, MyHashSetTwo


class TestMyHashSet(unittest.TestCase):
    def test_example_1(self):
        hs = MyHashSet()
        hs.add(key=1)
        hs.add(key=2)
        assert hs.contains(key=1) is True
        assert hs.contains(key=3) is False
        hs.add(key=2)
        assert hs.contains(key=2) is True
        hs.remove(key=2)
        assert hs.contains(key=2) is False
        hs.remove(key=99)
        assert hs.contains(key=99) is False

    def test_example_2(self):
        hs = MyHashSetTwo()
        hs.add(key=1)
        hs.add(key=2)
        assert hs.contains(key=1) is True
        assert hs.contains(key=3) is False
        hs.add(key=2)
        assert hs.contains(key=2) is True
        hs.remove(key=2)
        assert hs.contains(key=2) is False
        hs.remove(key=99)
        assert hs.contains(key=99) is False

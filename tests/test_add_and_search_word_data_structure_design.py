import unittest

from add_and_search_word_data_structure_design import WordDictionary, WordDictionaryTwo


class TestAddAndSearchWordDataStructureDesign(unittest.TestCase):
    def test_example_1(self):
        wd = WordDictionary()
        wd.addWord(word="bad")
        wd.addWord(word="dad")
        wd.addWord(word="mad")
        assert wd.search(word="pad") is False
        assert wd.search(word="bad") is True
        assert wd.search(word=".ad") is True
        assert wd.search(word="b..") is True
        assert wd.search(word="b") is False
        assert wd.search(word="bad.") is False

    def test_example_2(self):
        wd = WordDictionaryTwo()
        wd.addWord(word="bad")
        wd.addWord(word="dad")
        wd.addWord(word="mad")
        assert wd.search(word="pad") is False
        assert wd.search(word="bad") is True
        assert wd.search(word=".ad") is True
        assert wd.search(word="b..") is True
        assert wd.search(word="b") is False
        assert wd.search(word="bad.") is False

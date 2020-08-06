import re


class WordDictionary:
    # This leads to TLE
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot
        character '.' to represent any one letter.
        """
        for wd in self.words:
            if re.compile(pattern=word).fullmatch(wd):
                return True
        return False


class WordDictionaryTwo:
    def __init__(self):
        self.trie = {"_root": dict()}

    def addWord(self, word: str) -> None:
        dic = self.trie.get("_root")
        for ch in word:
            dic = dic.setdefault(ch, dict())
        dic["_end"] = "_end"

    def search(self, word: str, dic: dict = None) -> bool:
        if dic is None:
            dic = self.trie.get("_root")

        for i, wd in enumerate(word):
            if wd == ".":
                for ch in dic:
                    if ch != "_end" and self.search(
                        word=word[i + 1 :], dic=dic.get(ch)
                    ):
                        return True
                return False
            else:
                if wd not in dic:
                    return False
                dic = dic[wd]
        return "_end" in dic


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

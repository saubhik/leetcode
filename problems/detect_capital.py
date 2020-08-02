import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == "":
            return True

        first_letter = word[0]

        if "A" <= first_letter <= "Z":
            return self.checkAll(word=word[1:], isupper=False) or self.checkAll(
                word=word[1:], isupper=True
            )
        else:
            return self.checkAll(word=word, isupper=False)

    def checkAll(self, word: str, isupper: bool):
        for ch in word:
            if isupper:
                if ch.islower():
                    return False
            else:
                if ch.isupper():
                    return False
        return True


class SolutionTwo:
    def detectCapitalUse(self, word: str) -> bool:
        # return (
        #     re.fullmatch(pattern=r"[A-Z]*|[a-z]*|[A-Z][a-z]*", string=word)
        #     is not None
        # )
        return re.fullmatch(pattern=r"[A-Z]*|.[a-z]*", string=word) is not None

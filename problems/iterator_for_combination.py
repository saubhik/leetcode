from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        comb = combinations(iterable=characters, r=combinationLength)
        self.comb_list = []
        for tup in comb:
            self.comb_list.append("".join(tup))
        self.it = 0

    def next(self) -> str:
        result = self.comb_list[self.it]
        self.it += 1
        return result

    def hasNext(self) -> bool:
        return self.it < len(self.comb_list)


class CombinationIteratorII:
    # improvement over previous one
    def __init__(self, characters: str, combinationLength: int):
        self.combs = list(
            map("".join, combinations(iterable=characters, r=combinationLength))
        )[::-1]

    def next(self) -> str:
        return self.combs.pop()

    def hasNext(self) -> bool:
        return bool(self.combs)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

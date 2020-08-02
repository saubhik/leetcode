from typing import Dict


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map: Dict[int, bool] = dict()

    def add(self, key: int) -> None:
        self.hash_map[key] = True

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            del self.hash_map[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hash_map.get(key, False)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSetTwo:
    def __init__(self):
        self.hash_set = bytearray(1000001)

    def add(self, key: int) -> None:
        self.hash_set[key] = True

    def remove(self, key: int) -> None:
        self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        if self.hash_set[key]:
            return True
        else:
            return False

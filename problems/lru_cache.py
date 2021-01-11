from typing import Optional
from unittest import TestCase


class DoublyLinkedListNode:
    def __init__(
        self,
        key: int,
        value: int,
        prev: Optional["DoublyLinkedListNode"] = None,
        next: Optional["DoublyLinkedListNode"] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class CacheData:
    def __init__(self):
        # head -> first -> ... -> last -> tail
        # Pseudo-head and pseudo-tail improves logic.
        self.head = DoublyLinkedListNode(key=-1, value=-1, prev=None)
        self.tail = DoublyLinkedListNode(key=-1, value=-1, next=None)
        self.head.next = self.tail
        self.tail.prev = self.head

        # Hashmap from key to corresponding Double Linked List node.
        self.hashmap = {}

    def insert(self, key: int, value: int) -> None:
        # Add node to last.
        last = self.tail.prev
        node = DoublyLinkedListNode(key=key, value=value, prev=last, next=self.tail)
        last.next = node
        self.tail.prev = node

        self.hashmap[key] = node

    def get(self, key: int) -> int:
        # assert key in hashmap
        node = self.hashmap[key]
        return node.value

    def update(self, key: int, value: int) -> None:
        # assert key in self.hashmap
        node = self.hashmap[key]
        node.value = value

    def move_to_last(self, key: int) -> None:
        # assert key in self.hashmap
        node = self.hashmap[key]

        # Remove node from it's place in the Double Linked List
        node.prev.next = node.next
        node.next.prev = node.prev

        # Move node to last
        last = self.tail.prev
        # Establish connections between last & node.
        last.next = node
        node.prev = last
        # Establish connections between node & self.tail.
        node.next = self.tail
        self.tail.prev = node

    def pop_first(self) -> None:
        # Remove first node from Double Linked List
        # assert self.head.next.next is not None
        first, second = self.head.next, self.head.next.next
        self.head.next = second
        second.prev = self.head

        # Remove first node's content from the hashmap.
        self.hashmap.pop(first.key)

    def __len__(self) -> int:
        return len(self.hashmap)

    def __contains__(self, key: int) -> bool:
        return key in self.hashmap


class LRUCache:
    def __init__(self, capacity: int):
        self.data = CacheData()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # Get value of key if present.
        # Also make this most recently used.
        # Otherwise, return -1.
        if key in self.data:
            self.data.move_to_last(key=key)
            return self.data.get(key=key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Update value for key if present. Otherwise add key-value pair.
        # Also make this most recently used.
        if key in self.data:
            self.data.update(key=key, value=value)
            self.data.move_to_last(key=key)
        else:
            self.data.insert(key=key, value=value)
            if len(self.data) > self.capacity:
                self.data.pop_first()


class TestLRUCache(TestCase):
    def test_example_1(self):
        obj = LRUCache(capacity=2)
        obj.put(key=1, value=1)  # 1
        obj.put(key=2, value=2)  # 2 <-> 1
        assert obj.get(key=1) == 1  # 1 <-> 2
        obj.put(key=3, value=3)  # Evicts key=2. 3 <-> 1
        assert obj.get(key=2) == -1
        obj.put(key=4, value=4)  # Evicts key=1. 4 <-> 3.
        assert obj.get(key=1) == -1
        assert obj.get(key=3) == 3
        assert obj.get(key=4) == 4

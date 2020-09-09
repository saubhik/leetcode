from collections import deque


class MovingAverage:
    # Using double-ended queue (deque)
    # Space: O(size).
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])
        self.sum = 0
        self.size = size
        self.queue_len = 0

    def next(self, val: int) -> float:
        # Time: O(1).
        self.queue.append(val)
        self.sum += val
        self.queue_len += 1

        if self.queue_len > self.size:
            popped = self.queue.popleft()
            self.sum -= popped
            self.queue_len -= 1

        return self.sum / min(self.queue_len, self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


class MovingAverageTwo:
    # Using circular queue with array.
    # - Automatically discards the oldest element.
    # - Single pointer is enough to maintain head and tail.
    #
    # Time: O(1).
    # Space: O(size).
    def __init__(self, size: int):
        self.queue = [0] * size
        self.size = size
        self.head = -1
        self.sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.head = (self.head + 1) % self.size
        self.sum -= self.queue[self.head]
        self.queue[self.head] = val
        self.sum += val
        if self.count < self.size:
            self.count += 1
        return self.sum / self.count

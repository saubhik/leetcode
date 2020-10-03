from collections import deque


class RecentCounter:
    """
    Your RecentCounter object will be instantiated and called as such:
    obj = RecentCounter()
    param_1 = obj.ping(t)

    Example:
    Input
    ["RecentCounter", "ping", "ping", "ping", "ping"]
    [[], [1], [100], [3001], [3002]]
    Output
    [null, 1, 2, 3, 3]
    """

    def __init__(self):
        self.ping_ts = []
        self.length = 0

    def ping(self, t: int) -> int:
        # At any instant of time, self.ping_ts has maximum length
        # of 3001. So time complexity is O(1) and space complexity
        # is O(1).
        self.ping_ts.append(t)

        i, count = self.length, 0
        while i >= 0 and self.ping_ts[i] >= t - 3000:
            count, i = count + 1, i - 1

        self.ping_ts, self.length = self.ping_ts[i + 1 :], count

        return count


class RecentCounterOfficial:
    """
    == Overview ==
    We are given a sequence of ping calls, i.e. [t1, t2, ... tn], ordered by the
    chronological order of their arrival time.
    Given the current ping call ti, we are asked to count the number of previous calls
    that fall in the range [ti - 3000, ti].

    == Approach 1: Iteration over Sliding Window ==
    The idea is that we can use a container such as array or list to keep track of all
    the incoming ping calls. At each occasion of ping(t) call, first we append the call
    to the container, and then starting from the current call, we iterate backwards to
    count the calls that fall into the time range of [t-3000, t].

    Once the ping calls become outdated, i.e. out of the scope of [t - 3000, t], we do
    not need to keep them any longer in the container, since they will not contribute
    to the solution later.
    As a result, one optimization that we could do is that rather than keeping all the
    historical ping calls in the container, we could remove the outdated calls on the
    go, which can avoid overflow of the container and reduce the memory consumption to
    the least.

    In summary, out container will function like a sliding window over the ever-
    growing sequence of ping calls.

    == Algorithm ==
    To implement the sliding window, we could use deque in Python.
    Then the ping(t) function can be implemented in two steps:
        - Step 1: We append the current ping call to the tail of the sliding window.
        - Step 2: Starting from the head of the sliding window, we remove the outdated
        calls, until we come across a still valid ping call.
    As a result, the remaining calls in the sliding window are the ones that fall into
    the range [t-3000,t].

    == Complexity Analysis ==
    It is guaranteed that every call to ping uses a strictly larger value of t than
    before. Based on the above condition, the maximal number of elements in our sliding
    window would be 3000, which is also the maximal time difference between the head
    and the tail elements.

        - Time Complexity: O(1)
            - The main time complexity of our ping(t) function lies in the loop, which
            in the worst case would run 3000 iterations to pop out all outdated elements
            and in the best case a single iteration.
            - Therefore, for a single invocation of ping() functions, its
            time complexity if O(3000) = O(1).
            - If we assume that there is a ping call at each timestamp, then the cost of
            ping() is further amortized, where at each invocation, we would only need to
            pop out a single element, once the sliding window reaches its upper bound.
        - Space Complexity: O(1)
            - As we estimated before, the maximal size of our sliding window is 3000,
            which is a constant.
    """

    def __init__(self):
        self.slide_window = deque()
        self.length = 0

    def ping(self, t: int) -> int:
        self.slide_window.append(t)
        self.length += 1

        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()
            self.length -= 1

        return self.length

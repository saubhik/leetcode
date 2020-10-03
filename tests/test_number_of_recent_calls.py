import unittest

from number_of_recent_calls import RecentCounter, RecentCounterOfficial


class TestRecentCounter(unittest.TestCase):
    def test_example_1(self):
        recent_counter = RecentCounter()
        for t, expected in [(1, 1), (100, 2), (3001, 3), (3002, 3)]:
            assert recent_counter.ping(t=t) == expected

        recent_counter_official = RecentCounterOfficial()
        for t, expected in [(1, 1), (100, 2), (3001, 3), (3002, 3)]:
            assert recent_counter_official.ping(t=t) == expected

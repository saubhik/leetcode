import unittest

from meeting_rooms_ii import Solution


class TestMeetingRoomsII(unittest.TestCase):
    def test_example_1(self):
        assert Solution().minMeetingRooms(intervals=[[0, 30], [5, 10], [15, 20]]) == 2

    def test_example_2(self):
        assert Solution().minMeetingRooms(intervals=[[7, 10], [2, 4]]) == 1

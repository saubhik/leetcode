import unittest

from meeting_rooms import Solution


class TestMeetingRooms(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]])
            is False
        )

    def test_example_2(self):
        assert Solution().canAttendMeetings(intervals=[[7, 10], [2, 4]]) is True

import unittest

from robot_bounded_in_circle import Solution


class TestRobotBoundedInCircle(unittest.TestCase):
    def test_example_1(self):
        assert Solution().isRobotBounded(instructions="GGLLGG") is True

    def test_example_2(self):
        assert Solution().isRobotBounded(instructions="GG") is False

    def test_example_3(self):
        assert Solution().isRobotBounded(instructions="GL") is True

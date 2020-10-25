import unittest

from slowest_key import Solution


class TestSlowestKey(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd")
            == "c"
        )

    def test_example_2(self):
        assert (
            Solution().slowestKey(
                releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda"
            )
            == "a"
        )

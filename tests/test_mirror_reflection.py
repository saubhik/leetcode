from unittest import TestCase

from mirror_reflection import Solution


class TestMirrorReflection(TestCase):
    def test_example_1(self):
        assert Solution().mirrorReflection(p=2, q=1) == 2

    def test_example_2(self):
        assert Solution().mirrorReflection(p=5, q=3)

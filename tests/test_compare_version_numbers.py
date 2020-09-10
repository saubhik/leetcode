import unittest

from compare_version_numbers import Solution, SolutionTwo


class TestCompareVersionNumbers(unittest.TestCase):
    def test_example_1(self):
        assert Solution().compareVersion(version1="0.1", version2="1.1") == -1
        assert SolutionTwo().compareVersion(version1="0.1", version2="1.1") == -1

    def test_example_2(self):
        assert Solution().compareVersion(version1="1.0.1", version2="1") == 1
        assert SolutionTwo().compareVersion(version1="1.0.1", version2="1") == 1

    def test_example_3(self):
        assert Solution().compareVersion(version1="7.5.2.4", version2="7.5.3") == -1
        assert SolutionTwo().compareVersion(version1="7.5.2.4", version2="7.5.3") == -1

    def test_example_4(self):
        assert Solution().compareVersion(version1="1.01", version2="1.001") == 0
        assert SolutionTwo().compareVersion(version1="1.01", version2="1.001") == 0

    def test_example_5(self):
        assert Solution().compareVersion(version1="1.0", version2="1.0.0") == 0
        assert SolutionTwo().compareVersion(version1="1.0", version2="1.0.0") == 0

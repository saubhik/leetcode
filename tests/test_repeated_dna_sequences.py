import unittest

from repeated_dna_sequences import (
    Solution,
    OfficialSolutionApproach2,
    OfficialSolutionApproach3,
)


class TestRepeatedDNASequences(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findRepeatedDnaSequences(
            s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        ) == ["AAAAACCCCC", "CCCCCAAAAA"]
        assert set(
            OfficialSolutionApproach2().findRepeatedDnaSequences(
                s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
            )
        ) == {"CCCCCAAAAA", "AAAAACCCCC"}
        assert set(
            OfficialSolutionApproach3().findRepeatedDnaSequences(
                s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
            )
        ) == {"CCCCCAAAAA", "AAAAACCCCC"}

    def test_example_2(self):
        assert Solution().findRepeatedDnaSequences(s="AAAAAAAAAAAAA") == ["AAAAAAAAAA"]
        assert OfficialSolutionApproach2().findRepeatedDnaSequences(
            s="AAAAAAAAAAAAA"
        ) == ["AAAAAAAAAA"]
        assert OfficialSolutionApproach3().findRepeatedDnaSequences(
            s="AAAAAAAAAAAAA"
        ) == ["AAAAAAAAAA"]

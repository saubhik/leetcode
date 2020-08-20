import unittest

from goat_latin import Solution


class TestGoatLatin(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().toGoatLatin(S="I speak Goat Latin")
            == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        )

    def test_example_2(self):
        assert (
            Solution().toGoatLatin(S="The quick brown fox jumped over the lazy dog")
            == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa "
            "hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
        )

    def test_example_3(self):
        assert (
            Solution().toGoatLatin(
                S="Each word consists of lowercase and uppercase letters only"
            )
            == "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa "
            "uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa"
        )

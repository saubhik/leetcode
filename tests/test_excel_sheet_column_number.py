import unittest

from excel_sheet_column_number import Solution


class TestExcelSheetColumnNumber(unittest.TestCase):
    def test_example_1(self):
        assert Solution().titleToNumber(s="A") == 1
        assert Solution().titleToNumber(s="AB") == 28
        assert Solution().titleToNumber(s="ZY") == 701

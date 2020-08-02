import unittest

from subrectangle_queries import SubrectangleQueries, SubrectangleQueriesTwo


class TestSubrectangleQueries(unittest.TestCase):
    def test_example_1(self):
        obj = SubrectangleQueries(
            rectangle=[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
        )
        assert obj.getValue(row=0, col=2) == 1
        obj.updateSubrectangle(row1=0, col1=0, row2=3, col2=2, newValue=5)
        assert obj.getValue(row=0, col=2) == 5
        assert obj.getValue(row=3, col=1) == 5
        obj.updateSubrectangle(row1=3, col1=0, row2=3, col2=2, newValue=10)
        assert obj.getValue(row=3, col=1) == 10
        assert obj.getValue(row=0, col=2) == 5

    def test_example_2(self):
        obj = SubrectangleQueriesTwo(
            rectangle=[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
        )
        assert obj.getValue(row=0, col=2) == 1
        obj.updateSubrectangle(row1=0, col1=0, row2=3, col2=2, newValue=5)
        assert obj.getValue(row=0, col=2) == 5
        assert obj.getValue(row=3, col=1) == 5
        obj.updateSubrectangle(row1=3, col1=0, row2=3, col2=2, newValue=10)
        assert obj.getValue(row=3, col=1) == 10
        assert obj.getValue(row=0, col=2) == 5

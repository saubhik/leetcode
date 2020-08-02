from typing import List


class SubrectangleQueries:
    # Your SubrectangleQueries object will be instantiated and called as such:
    # obj = SubrectangleQueries(rectangle)
    # obj.updateSubrectangle(row1,col1,row2,col2,newValue)
    # param_2 = obj.getValue(row,col)

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


class SubrectangleQueriesTwo:
    # What if there are a lot of update ops, and only a few getValue ops?
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.history = list()

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        self.history.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for row1, col1, row2, col2, newValue in reversed(self.history):
            if row1 <= row <= row2 and col1 <= col <= col2:
                return newValue

        return self.rectangle[row][col]

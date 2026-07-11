class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # [3, 3, 4, 8, 10]
        # [5,11, 14, 16, 17]
        # [1, 3, 3, 4, 9]
        # [4, 5, 5, 6, 13]
        # [1, 1, 4, 4, 9]
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSums = [[] for _ in range(cols) for _ in range(rows)] 

        for i in range(rows):
            currSum = 0
            for j in range(cols):
                currSum += matrix[i][j]
                self.prefixSums[i].append(currSum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        currSum = 0
        for i in range(row1, row2 + 1):
            if col1 > 0:
                currSum += self.prefixSums[i][col2] - self.prefixSums[i][col1 -1]
            else:
                currSum += self.prefixSums[i][col2]
        return currSum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
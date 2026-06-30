class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        numbers = set(['1','2','3','4','5','6','7','8','9'])

        def checkRow(row):
            numberSet = set()
            for i in range(cols):
                if board[row][i] in numbers:
                    if board[row][i] in numberSet:
                        return False
                    numberSet.add(board[row][i])
            
            return True
        
        def checkCol(col):
            numberSet = set()
            for i in range(rows):
                if board[i][col] in numbers:
                    if board[i][col] in numberSet:
                        return False
                    numberSet.add(board[i][col])
            return True
        
        def checkSubBox(row, col):
            numberSet = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] in numbers:
                        if board[i][j] in numberSet:
                            return False
                        numberSet.add(board[i][j])
            return True
        
        for i in range(rows):
            if not checkRow(i):
                return False
        
        for i in range(cols):
            if not checkCol(i):
                return False
        
        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                if not checkSubBox(i, j):
                    return False
        
        return True



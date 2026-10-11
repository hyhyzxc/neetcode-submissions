class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or board[i][j] == 'X':
                return
            
            visited.add((i, j))

            for x, y in dirs:
                nr, nc = i+x, j+y
                dfs(nr, nc)
        
        for i in range(cols):
            dfs(0, i) if board[0][i] == 'O' else None
            dfs(rows - 1, i) if board[rows-1][i] == 'O' else None
        
        for i in range(rows):
            dfs(i, 0) if board[i][0] == 'O' else None
            dfs(i, cols - 1) if board[i][cols-1] == 'O' else None
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'
        
        



        


from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        queue = deque([])

        for i in range(cols):
            if board[0][i] == 'O':
                queue.append((0, i))
            if board[rows-1][i] == 'O':
                queue.append((rows-1, i))
        
        for i in range(rows):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][cols-1] == 'O':
                queue.append((i, cols-1))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            for x, y in directions:
                newI, newJ = i+x, j+y
                if (newI >= 0 and newI < rows and newJ >= 0 and newJ < cols 
                    and (newI, newJ) not in visited and board[newI][newJ] == 'O'):
                    queue.append((newI, newJ))
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited:
                    board[i][j] = 'X'
        



        


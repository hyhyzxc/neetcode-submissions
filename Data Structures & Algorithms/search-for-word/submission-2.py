class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, wordIndex, visited):
            if wordIndex >= len(word):
                return True
                
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited:
                return False

            
            
            res = False
            if word[wordIndex] == board[i][j]:
                visited.add((i, j))

                res = (dfs(i+1, j, wordIndex + 1, visited.copy()) 
                    or dfs(i-1, j, wordIndex + 1, visited.copy()) 
                    or dfs(i, j+1, wordIndex + 1, visited.copy())
                    or dfs(i, j-1, wordIndex + 1, visited.copy()))

                visited.remove((i, j))
            
            return res
            
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0, set()):
                    return True
        
        return False

            

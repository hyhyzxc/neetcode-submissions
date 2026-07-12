class Solution:
    def totalNQueens(self, n: int) -> int:
        # (0, 1)
        # (1, 0)
        # (1, 2), (2, 3)
        res = 0

        def backtrack(r, blocked):
            nonlocal res
            if r >= n:
                res += 1
                return

            for c in range(n):
                if (r, c) in blocked:
                    continue

                copyBlocked = blocked.copy()

                for row in range(r+1, n):
                    copyBlocked.add((row, c))
                
                row, col = r, c

                while row < n and col >= 0:
                    copyBlocked.add((row, col))
                    row += 1
                    col -= 1
                
                row, col = r, c

                while row < n and col < n:
                    copyBlocked.add((row, col))
                    row += 1
                    col += 1
                
                backtrack(r+1, copyBlocked)
        
        backtrack(0, set())
        return res
                



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # two choices: put open bracket or put close bracket

        # if open bracket count == n: can only put close bracket

        # if open bracket count == 0: can only put open bracket
        res = []

        def dfs(openCount, closeCount, currArr):
            if openCount == n and closeCount == n:
                res.append(''.join(currArr))
                return
            elif openCount == n and closeCount < n:
                currArr.append(')')
                dfs(openCount, closeCount + 1, currArr.copy())
            elif openCount == 0:
                currArr.append('(')
                dfs(openCount + 1, closeCount, currArr.copy())
            else:
                # choose to put open bracket
                currArr.append('(')
                dfs(openCount + 1, closeCount, currArr.copy())
                currArr.pop()

                # choose to put close bracket
                if openCount > closeCount:
                    currArr.append(')')
                    dfs(openCount, closeCount + 1, currArr.copy())
                    currArr.pop()
        
        dfs(0, 0, [])
        return res
            



        
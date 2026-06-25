class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [-1] * n

        def dfs(i):
            if i < 0:
                return 1
            
            if dp[i] > -1:
                return dp[i]
            
            res = 0
            
            for j in range(i, -1, -1):
                if s[j: i+1] in wordDict:
                    res = dfs(j - 1)
                    if res:
                        dp[j] = 1
                        return res
            
            dp[i] = 0
            return res
        
        dfs(n-1)
        return dp[0] == 1
            

        
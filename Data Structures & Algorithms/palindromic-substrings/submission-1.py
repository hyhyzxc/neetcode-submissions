class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        res = 0
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j - i >= 2 and dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                    res += 1
                else:
                    if j - i <= 2 and s[i] == s[j]:
                        dp[i][j] = 1
                        res += 1

        return res

        
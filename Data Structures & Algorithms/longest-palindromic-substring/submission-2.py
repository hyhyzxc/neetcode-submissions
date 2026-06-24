class Solution:
    def longestPalindrome(self, s: str) -> str:
        #"aabbbbcc"
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        res = ""
        maxLen = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i >= 2:
                    dp[i][j] = 1 if s[i] == s[j] and dp[i+1][j-1] else 0
                else:
                    if i == j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 if s[i] == s[j] else 0

                if j-i+1 >= maxLen and dp[i][j]:
                    maxLen = j-i+1
                    res = s[i:j+1]
        
        return res

        

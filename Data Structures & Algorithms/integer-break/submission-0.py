class Solution:
    def integerBreak(self, n: int) -> int:
        # 2 -> 1 + 1 -> 1x1=1
        # 3 -> 1 + 2 -> 1x2=2
        # 4 -> 2 + 2 -> 2x2=4
        # 5 -> 3 + 2 -> 3x2=6
        # 6 -> f(5) * 1, f(4) * 2, f(3) * 3, f(2) * 4 -> 9
        # 12 -> f(6) * f(6)

        dp = [0] * (n+1)
        
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                dp[i] = max(dp[i], max(dp[j] * (i - j), j * (i - j)))
        
        return dp[n]
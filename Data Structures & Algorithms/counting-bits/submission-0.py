class Solution:
    def countBits(self, n: int) -> List[int]:
        # 000
        # 001
        # 010
        # 011
        # 100
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if i == offset * 2:
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp
        
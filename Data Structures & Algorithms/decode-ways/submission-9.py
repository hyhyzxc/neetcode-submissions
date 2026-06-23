class Solution:
    def numDecodings(self, s: str) -> int:
        # 112453
        # 5,3,2,1,1,1

        # 1 1 2 4 5 3
        # 11 2 4 5 3
        # 1 12 4 5 3
        # 1 1 24 5 3

        dp = [0] * len(s)

        def isValid(s):
            validSet = set([str(i) for i in range(1, 27)])
            return s in validSet
        
        dp[-1] = 1 if isValid(s[-1]) else 0
        if len(s) == 1:
            return dp[0]
        dp[-2] = dp[-1] + 1 if isValid(s[len(s) - 2:]) else dp[-1]
        if s[-2] == "0":
            dp[-2] = 0

        for i in range(len(s) - 3, -1, -1):
            if not isValid(s[i]) or s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if isValid(s[i:i+2]):
                    dp[i] += dp[i+2]
        
        return dp[0]



         
        
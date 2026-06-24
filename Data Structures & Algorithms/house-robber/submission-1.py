class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        res = 0

        def dfs(currIndex):
            nonlocal res
            if currIndex >= len(nums):
                return 0
            
            if dp[currIndex] != -1:
                return dp[currIndex]
            
            maxMoney = max(dfs(currIndex + 1), dfs(currIndex + 2) + nums[currIndex])
            res = max(maxMoney, res)
            dp[currIndex] = maxMoney

            return maxMoney
        
        dfs(0)

        return res
        
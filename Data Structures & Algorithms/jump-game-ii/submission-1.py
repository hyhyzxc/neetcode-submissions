class Solution:
    def jump(self, nums: List[int]) -> int:
        res = len(nums)
        dp = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if i in dp:
                return dp[i]
            
            maxPosition = nums[i]
            dist = len(nums)

            for jump in range(1, maxPosition + 1):
                dist = min(dfs(i + jump) + 1, dist)
            
            dp[i] = dist
            return dp[i]

        return dfs(0)

            


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        # 1 -> (1)
        # 2 -> (1,1), (2)
        # 3 -> num ways to form 0 + num ways to form 2 + num ways to form 1 = 1 + 2 + 1 = 4
        # 4 -> num ways to form 3 + num ways to form 2 + num ways to form 1 = 4 + 2 + 1 = 7

        def dfs(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if target in dp:
                return dp[target]
            
            res = 0
            for num in nums:
                res += dfs(target - num)
            
            dp[target] = res
            return res
        
        dp[0] = 1
        for i in range(1, target + 1):
            dp[i] = dfs(i)
        return dp[target]
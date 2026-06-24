class Solution:
    def rob(self, nums: List[int]) -> int:        
        res = 0
        dp = [-1] * (len(nums) - 1)
        dp2 = [-1] * (len(nums) - 1)
        n = len(nums)
        if n == 1:
            return nums[0]

        def dfs(i, nums, dp):
            nonlocal res

            if i >= len(nums):
                return 0

            if dp[i] != -1:
                return dp[i]
            
            currAmt = max(dfs(i + 1, nums, dp), nums[i] + dfs(i + 2, nums, dp))
            res = max(res, currAmt)

            dp[i] = currAmt
            return currAmt
        
        dfs(0, nums[:-1], dp)
        dfs(0, nums[1:], dp2)

        return res
        
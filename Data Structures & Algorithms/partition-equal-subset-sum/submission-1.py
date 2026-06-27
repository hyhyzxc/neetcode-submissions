class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums)

        if arrSum % 2: 
            return False
        
        target = arrSum // 2
        n = len(nums)

        dp = [[-1 for i in range(target + 1)] for j in range(n + 1)]
        
        def dfs(i, target):
            if i >= n or target < 0:
                return False
            
            if nums[i] == target:
                return True
            
            if dp[i][target] != -1:
                return dp[i][target]
            
            dp[i][target] = dfs(i+1, target - nums[i]) or dfs(i+1, target)

            return dp[i][target]
        
        return dfs(0, target)


        


        

        

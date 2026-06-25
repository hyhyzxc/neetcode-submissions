class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #we need to keep track of last added element in subsequence
        n = len(nums)
        dp = [-1 for i in range(n)]

        def dfs(currIndex):
            if currIndex >= n:
                return 0
            
            if dp[currIndex] != -1:
                return dp[currIndex]
            
            res = 1
            
            for nextIndex in range(currIndex + 1, n):
                if nums[nextIndex] > nums[currIndex]:
                    res = max(res, 1 + dfs(nextIndex))
            
            dp[currIndex] = res
            return res
            
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        
        return res


        
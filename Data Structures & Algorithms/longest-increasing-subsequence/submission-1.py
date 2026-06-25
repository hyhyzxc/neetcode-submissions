class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #we need to keep track of last added element in subsequence
        n = len(nums)
        dp = [[-1 for i in range(n)] for j in range(n)]

        def dfs(currIndex, prevIndex):
            if currIndex >= n:
                return 0
            
            if dp[currIndex][prevIndex] > -1:
                return dp[currIndex][prevIndex]
            
            res = 0

            # include current index
            if prevIndex == -1 or nums[currIndex] > nums[prevIndex]:
                res = dfs(currIndex + 1, currIndex) + 1

            # don't include current index
            res = max(res, dfs(currIndex + 1, prevIndex))
            dp[currIndex][prevIndex] = res

            return res
        
        return dfs(0, -1)


        
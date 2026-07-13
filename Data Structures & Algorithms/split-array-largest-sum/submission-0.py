class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # [2,4,10,1,5]
        # [2,4,10], [1,5]
        #brute force:
        # find k-1 cuts to the array, where in each cut, we reset currSum count, return min currSum

        n = len(nums)
        res = float("inf")
        dp = {}

        def dfs(i, k):
            if k == 1:
                return sum(nums[i:])
            
            if (i, k) in dp:
                return dp[(i, k)]
            
            res = float("inf")
            currSum = 0
            for index in range(i, n):
                currSum += nums[index]
                remaining = dfs(index+1, k-1)
                res = min(res, max(currSum, remaining))
            
            dp[(i, k)] = res
            return res
        
        res = min(res, dfs(0, k))
        return res
        
            


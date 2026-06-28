class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        res = 0
        
        def dfs(i, currTarget):
            nonlocal res
            if currTarget == target and i >= len(nums):
                return 1

            if i >= len(nums):
                return 0
            
            if (i, currTarget) in dp:
                return dp[(i, currTarget)]
            
            # choose positive for current i
            positive = dfs(i + 1, currTarget + nums[i])

            # choose negative for current i
            negative = dfs(i + 1, currTarget - nums[i])

            dp[(i, currTarget)] = positive + negative
            return dp[(i, currTarget)]
        
        dfs(0, 0)

        return dp[(0, 0)]


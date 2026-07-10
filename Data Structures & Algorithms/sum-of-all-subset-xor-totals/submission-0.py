class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def dfs(i, currSum):
            nonlocal res

            if i >= n:
                res += currSum
                return
            
            # include current value in current sum
            dfs(i+1, currSum ^ nums[i])

            # skip current value
            dfs(i+1, currSum)
        
        dfs(0, 0)
        return res
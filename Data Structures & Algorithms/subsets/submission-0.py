class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, currRes):
            if i >= len(nums):
                res.append(currRes)
                return
            
            currRes.append(nums[i])
            dfs(i+1, currRes.copy())

            currRes.pop()
            dfs(i+1, currRes.copy())
        
        dfs(0, [])
        return res


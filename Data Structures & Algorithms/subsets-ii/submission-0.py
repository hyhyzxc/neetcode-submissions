class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(i, currArr):
            if i >= len(nums):
                res.append(currArr)
                return
            
            # take the current value
            currArr.append(nums[i])
            dfs(i+1, currArr.copy())
            currArr.pop()

            # skip the current value, skip through all duplicates
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, currArr.copy())
        
        dfs(0, [])
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, currList, target):
            if target == 0:
                res.append(currList)
                return
            
            if target - nums[i] < 0:
                return
            
            # include i
            currVal = nums[i]
            if target - nums[i] >= 0:
                currList.append(nums[i])
                dfs(i, currList.copy(), target - nums[i])
                currList.pop()

            # exclude i
            for j in range(i + 1, len(nums)):
                if target - nums[j] >= 0:
                    currList.append(nums[j])
                    dfs(j, currList.copy(), target - nums[j])
                    currList.pop()
            
        dfs(0, [], target)
        return res
        

            

        
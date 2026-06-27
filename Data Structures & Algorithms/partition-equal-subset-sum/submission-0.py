class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums)

        if arrSum % 2: 
            return False
        
        target = arrSum / 2
        n = len(nums)
        
        def dfs(i, target):
            if i >= n or target < 0:
                return False
            
            if nums[i] == target:
                return True
            
            return dfs(i+1, target - nums[i]) or dfs(i+1, target)
        
        return dfs(0, target)


        


        

        

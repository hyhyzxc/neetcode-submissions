class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = nums[0]
        n = len(nums)

        for i in range(1, n):
            if currSum < 0:
                currSum = 0

            currSum += nums[i]
            res = max(currSum, res)
        
        return res
            

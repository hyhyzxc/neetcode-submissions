class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        n = len(nums)

        l, r = 0, 0
        currSum = 0

        while r < len(nums):
            currSum += nums[r]
            while l <= r and currSum >= target:
                res = min(r - l + 1, res)
                currSum -= nums[l]
                l += 1
            r += 1
        
        return res if res != float("inf") else 0
            
            
        
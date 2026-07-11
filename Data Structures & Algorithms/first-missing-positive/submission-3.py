class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        
        for num in nums:
            index = abs(num) - 1
            if index >= 0 and index < len(nums):
                if nums[index] == 0:
                    nums[index] = - (len(nums) + 1)
                elif nums[index] > 0:
                    nums[index] *= -1

        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums) + 1
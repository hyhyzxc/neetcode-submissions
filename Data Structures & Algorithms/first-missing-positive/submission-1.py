class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxRange = len(nums) + 1

        for i in range(1, maxRange + 1):
            if i not in nums:
                return i
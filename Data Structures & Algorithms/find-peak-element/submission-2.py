class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if m + 1 < len(nums) and nums[m] >= nums[m + 1]:
                r = m - 1
            else:
                l = m + 1
        
        return min(l, len(nums) - 1)

        
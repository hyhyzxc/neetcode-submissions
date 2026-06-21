class Solution:
    def findMin(self, nums: List[int]) -> int:
        currMin = nums[0]

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2

            if mid < len(nums) - 1 and nums[mid+1] < nums[mid]:
                return nums[mid+1]
            if nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            
        
        return currMin
        
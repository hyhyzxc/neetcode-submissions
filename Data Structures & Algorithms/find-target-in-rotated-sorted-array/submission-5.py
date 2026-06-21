class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first, find the pivot
        # then perform binary search on the correct side
        l = 0
        r = len(nums) - 1
        #3,5,6,0,1,2
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        
        return -1

        
        
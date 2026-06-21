class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first, find the pivot
        # then perform binary search on the correct side
        l = 0
        r = len(nums) - 1

        pivot = len(nums)

        while l <= r:
            mid = (l + r) // 2
            if mid < len(nums) - 1 and nums[mid + 1] < nums[mid]:
                pivot = mid + 1
                break
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        
        left = nums[:pivot]
        right = nums[pivot:]
        
        def searchTarget(values, target, l, r):
            if not values:
                return -1


            while l <= r:
                mid = (l + r) // 2
                if values[mid] == target:
                    return mid
                elif values[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1
        
        if left and right:
            if target < left[0]:
                return searchTarget(nums, target, pivot, len(nums) - 1) 
            else:
                return searchTarget(nums, target, 0, pivot - 1) 
        
        elif left and not right:
            return searchTarget(nums, target, 0, pivot - 1) 
        
        elif right and not left:
            return searchTarget(nums, target, pivot, len(nums) - 1) 
        
        return -1
        



        
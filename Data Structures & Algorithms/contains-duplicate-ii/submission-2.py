from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, min(k, len(nums) - 1)

        countMap = set()
        for i in range(l, r+1):
            if nums[i] in countMap:
                return True
            countMap.add(nums[i])
        
        while True:
            countMap.remove(nums[l])
            l += 1
            r += 1
            if r >= len(nums):
                return False

            if nums[r] in countMap:
                return True
            countMap.add(nums[r])
        
        
        
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            difference = target - num

            if num in hashMap:
                return [hashMap[num], i]
            
            hashMap[difference] = i
        

        
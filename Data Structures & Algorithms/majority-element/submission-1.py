from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        n = len(nums)
        currMax = 0
        res = 0

        for num in nums:
            countMap[num] += 1
            if countMap[num] >= currMax:
                currMax = countMap[num]
                res = num
        
        return res

        
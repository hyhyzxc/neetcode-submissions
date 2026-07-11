from collections import defaultdict
class Solution: 
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3

        countMap = defaultdict(int)

        for num in nums:
            countMap[num] += 1

            if len(countMap) <= 2:
                continue
            
            newCountMap = defaultdict(int)
            for num in countMap:
                if countMap[num] > 1:
                    newCountMap[num] = countMap[num] - 1
            countMap = newCountMap
        
        counts = defaultdict(int)
        for num in nums:
            if countMap[num] > 0:
                counts[num] += 1
        
        res = []

        for num in counts:
            if counts[num] > target:
                res.append(num)
        return res


                
                
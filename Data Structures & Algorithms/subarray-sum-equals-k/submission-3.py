from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countMap = defaultdict(int)
        countMap[0] += 1

        currSum = 0
        res = 0
        for num in nums:
            currSum += num
            res += countMap[currSum - k]
            countMap[currSum] += 1
        
        return res

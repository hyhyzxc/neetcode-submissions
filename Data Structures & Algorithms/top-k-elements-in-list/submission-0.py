import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1
        
        countArr = []
        for num in hashMap:
            countArr.append((hashMap[num], num))
        
        countArr = sorted(countArr, key = lambda x: x[0], reverse = True)
        return [x[1] for x in countArr[:k]]
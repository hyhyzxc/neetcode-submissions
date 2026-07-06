from collections import defaultdict
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        countMap = defaultdict(int)

        for num in hand:
            countMap[num] += 1
        
        minHeap = []

        for num in countMap:
            heapq.heappush(minHeap, num)
        
        i = 0
        for _ in range(len(hand) // groupSize):
            group = [minHeap[0]]
            countMap[minHeap[0]] -= 1
            if countMap[minHeap[0]] == 0:
                heapq.heappop(minHeap)
            
            while len(group) != groupSize:
                nextNumber = group[-1] + 1
                if countMap[nextNumber] == 0:
                    return False
                
                countMap[nextNumber] -= 1
                if countMap[nextNumber] == 0 and nextNumber == minHeap[0]:
                    heapq.heappop(minHeap)
                
                group.append(nextNumber)
        
        return True

            

            

        
        return True


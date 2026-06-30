import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            x, y = point[0], point[1]
            distance = self.findDistanceFromOrigin(x, y)
            
            if len(maxHeap) >= k:
                if distance < -maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-distance, x, y))
            else:
                heapq.heappush(maxHeap, (-distance, x, y))
        
        res = []
        for dist, x, y in maxHeap:
            res.append([x, y])
        
        return res



    def findDistanceFromOrigin(self, x, y):
        return math.sqrt(pow(x, 2) + pow(y, 2))
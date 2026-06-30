from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = defaultdict(int)

        if not tasks:
            return 0

        for task in tasks:
            freqMap[task] += 1
        
        frequencies = [(freqMap[x], x) for x in freqMap]
        frequencies.sort(reverse = True)

        heap = [] # (next available time, - frequency)

        for task in freqMap:
            heapq.heappush(heap, (0, -freqMap[task]))
        
        currTime = 0
       
        while heap:
            nextTime, freq = heap[0][0], -heap[0][1]
            if nextTime > currTime:
                currTime += nextTime - currTime
            else:
                heapq.heappop(heap)
                if freq - 1 > 0:
                    heapq.heappush(heap, (nextTime + n + 1, -(freq - 1)))
                currTime += 1
            
        return currTime




        
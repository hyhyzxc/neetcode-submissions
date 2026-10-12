from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countMap = defaultdict(int)

        for task in tasks:
            countMap[task] += 1
        
        # heap to store executable tasks
        # queue to store pending tasks to be inserted

        heap = [-countMap[task] for task in countMap]
        heapq.heapify(heap)
        queue = deque([])
        currTime = 0

        while heap or queue:
            currTime += 1

            if heap:
                freq = heapq.heappop(heap)
                if freq + 1 < 0:
                    queue.append((currTime + n, freq + 1))
            
            if queue and queue[0][0] == currTime:
                time, freq = queue.popleft()
                heapq.heappush(heap, freq)
        
        return currTime
            



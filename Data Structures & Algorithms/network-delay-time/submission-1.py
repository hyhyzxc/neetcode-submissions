import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for time in times:
            ui, vi, ti = time[0], time[1], time[2]
            adjList[ui].append((ti, vi))
        
        heap = [(0, k)]
        visited = set()
        res = 0

        while heap:
            cost, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            visited.add(curr)
            res = cost
            for neighbourCost, neighbour in adjList[curr]:
                if neighbour not in visited:
                    heapq.heappush(heap, (neighbourCost + cost, neighbour))
        
        return res if len(visited) == n else -1


        
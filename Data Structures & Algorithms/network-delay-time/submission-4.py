import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        res = 0

        adjList = defaultdict(list)

        for time in times:
            src, dest, dist = time[0], time[1], time[2]
            adjList[src].append((dist, dest))
        
        minHeap = [(0, k)]

        while minHeap:
            if len(visited) == n:
                return res
            
            cost, node = heapq.heappop(minHeap)
            res = max(cost, res)
            if node in visited:
                continue

            visited.add(node)

            for neighbourCost, neighbourNode in adjList[node]:
                if neighbourNode not in visited:
                    heapq.heappush(minHeap, (neighbourCost + cost, neighbourNode))
        
        return cost if len(visited) == n else -1


        
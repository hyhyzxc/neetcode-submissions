import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # generate adj list
        adjList = defaultdict(list)
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        visited = set()
        minHeap = [(0, 0)]
        cost = 0

        while True:
            if len(visited) == n:
                return cost
            
            currCost, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            cost += currCost
            visited.add(node)

            for neighbourCost, neighbourNode in adjList[node]:
                if neighbourNode not in visited:
                    heapq.heappush(minHeap, (neighbourCost, neighbourNode))
            



from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for flight in flights:
            source, dest, cost = flight[0], flight[1], flight[2]
            adjList[source].append((cost, dest))
        
        distances = [float("inf") for _ in range(n)]

        minHeap = [(0, src, -1)]
        visited = set()

        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)

            distances[node] = min(distances[node], cost)
            if node == dst:
                return cost

            visited.add(node)

            for neighbourCost, neighbourNode in adjList[node]:
                if neighbourNode != dst:
                    if stops + 1 < k:
                        heapq.heappush(minHeap, (neighbourCost + cost, neighbourNode, stops + 1))
                else:
                    heapq.heappush(minHeap, (neighbourCost + cost, neighbourNode, stops))
        
        return -1

            

        

        
        
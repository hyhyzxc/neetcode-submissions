from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 0 - 1 - 3 - 2
        #     |
        #     4
    
        heights = [0] * n

        adjList = defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        queue = deque([]) #node, curr height

        for i in range(n):
            queue.append((i, 0))
            visited = set()
            while queue:
                currNode, currHeight = queue.popleft()
                visited.add(currNode)
                heights[i] = max(heights[i], currHeight)
                for neighbourNode in adjList[currNode]:
                    if neighbourNode not in visited:
                        queue.append((neighbourNode, currHeight + 1))
        
        minHeight = min(heights)
        res = []

        for i, height in enumerate(heights):
            if height == minHeight:
                res.append(i)
        
        return res

        
        
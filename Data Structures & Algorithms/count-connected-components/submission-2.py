from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = defaultdict(list)

        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)

            for neighbor in adjList[i]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res

        
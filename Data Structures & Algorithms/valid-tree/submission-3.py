from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adjList[n1].add(n2)
            adjList[n2].add(n1)
        

        queue = deque([0])
        visited = set()
        # use bfs, check if there are cycles
 
        #visited = 0,1
        #queue = 2,3,4
        while queue:
            curr = queue.pop()
            if curr in visited:
                return False
            visited.add(curr)
            for neighbor in adjList[curr]:
                if neighbor in visited:
                    return False
                adjList[neighbor].remove(curr)
                queue.append(neighbor)
            
        return len(visited) == n
        
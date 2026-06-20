from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adjList[n1].add(n2)
            adjList[n2].add(n1)
        

        stack = [(0, None)]
        visited = set()
        # use bfs, check if there are cycles

        while stack:
            curr, parent = stack.pop()
            visited.add(curr)

            for neighbor in adjList[curr]:
                if neighbor not in visited:
                    stack.append((neighbor, curr))
                else:
                    if neighbor != parent:
                        return False
        
        return len(visited) == n

        
        
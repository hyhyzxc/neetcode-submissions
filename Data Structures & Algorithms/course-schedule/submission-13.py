from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)
        visited = set()

        for dest, src in prerequisites:
            adjList[src].append(dest)
            inDegrees[dest] += 1
        
        queue = deque([])

        for i in range(numCourses):
            queue.append(i) if inDegrees[i] == 0 else None
        
        while queue:
            curr = queue.popleft()
            visited.add(curr)

            for neighbour in adjList[curr]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0 and neighbour not in visited:
                    queue.append(neighbour)
        
        return len(visited) == numCourses
            


        
        

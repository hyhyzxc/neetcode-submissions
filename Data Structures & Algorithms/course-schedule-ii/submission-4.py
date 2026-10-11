from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)

        for dest, src in prerequisites:
            adjList[src].append(dest)
            inDegrees[dest] += 1
        
        queue = deque([])
        res = []
        visited = set()

        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neighbour in adjList[curr]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0 and neighbour not in visited:
                    queue.append(neighbour)
        
        return res if len(res) == numCourses else []
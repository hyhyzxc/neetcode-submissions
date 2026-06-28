from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)

        for prereq in prerequisites:
            n1, n2 = prereq[0], prereq[1]
            adjList[n2].append(n1)
            inDegrees[n1] += 1
        
        queue = deque([])
        
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
        
        res = []
        visited = set()
        while queue:
            curr = queue.popleft()
            res.append(curr)
            visited.add(curr)

            for neighbour in adjList[curr]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0 and neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        
        return res if len(res) == numCourses else []
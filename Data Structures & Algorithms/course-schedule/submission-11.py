from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)

        for prereq in prerequisites:
            i, j = prereq[0], prereq[1]
            adjList[i].append(j)
            inDegrees[j] += 1
        
        queue = deque([])

        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
        
        visited = set()
        while queue:
            curr = queue.popleft()
            visited.add(curr)

            for neighbour in adjList[curr]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    queue.append(neighbour)
        
        return len(visited) == numCourses
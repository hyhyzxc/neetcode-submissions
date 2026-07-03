from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #1 -> 0
        #0 -> 1
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)

        for prereq in prerequisites:
            src, dest = prereq[1], prereq[0]
            adjList[src].append(dest)
            inDegrees[dest] += 1
        
        queue = deque([])
        visited = set()

        for course in range(numCourses):
            if inDegrees[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            visited.add(course)
            for neighbour in adjList[course]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    queue.append(neighbour)
        
        return len(visited) == numCourses

        

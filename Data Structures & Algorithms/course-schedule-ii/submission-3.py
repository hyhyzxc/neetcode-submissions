from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)

        for prereq in prerequisites:
            src, dest = prereq[1], prereq[0]
            adjList[src].append(dest)
            inDegrees[dest] += 1
        
        path = []

        queue = deque([])

        for course in range(numCourses):
            if inDegrees[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.pop()
            path.append(course)
            for neighbour in adjList[course]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(path) == numCourses:
            return path
        else:
            return []

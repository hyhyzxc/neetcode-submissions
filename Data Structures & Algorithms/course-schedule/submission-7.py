from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        queue = deque([])
        topo = [0] * numCourses
        done = []

        for prereq in prerequisites:
            i, j = prereq[0], prereq[1]
            adjList[i].append(j)
            topo[j] += 1
        
        for i in range(numCourses):
            if topo[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            done.append(curr)
            for neighbor in adjList[curr]:
                topo[neighbor] -= 1
                if topo[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(done) == numCourses
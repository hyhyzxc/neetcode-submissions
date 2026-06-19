from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        done = set()

        for prereq in prerequisites:
            i, j = prereq[0], prereq[1]
            adjList[i].append(j)
        
        def dfs(i, visited):
            if i in visited:
                return False
            if i in done:
                return True
            
            visited.add(i)
            for neighbor in adjList[i]:
                if neighbor not in done:
                    if not dfs(neighbor, visited):
                        return False

            done.add(i)
            return True
        
        for i in range(numCourses + 1):
            res = dfs(i, set())
            if not res:
                return False
                
        return True

        
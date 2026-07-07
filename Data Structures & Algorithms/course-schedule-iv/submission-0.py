from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 3 -> 2 -> 1 -> 0
        # for query, find if query[0] has path to query[1]
        # in dfs, dfs function can return a list of reachable nodes from i

        reachable_nodes = [set()] * numCourses

        adjList = defaultdict(list)

        for src, dest in prerequisites:
            adjList[src].append(dest)

        def dfs(i):
            visited = set()
            visited.add(i)

            for neighbour in adjList[i]:
                if neighbour not in visited:
                    visited = visited.union(dfs(neighbour))
            
            return visited
        
        for node in range(numCourses):
            reachable_nodes[node] = dfs(node)
        
        res = []
        for src, dest in queries:
            res.append(dest in reachable_nodes[src])
        
        return res





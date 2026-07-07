from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for equation, value in zip(equations, values):
            n1, n2 = equation[0], equation[1]
            adjList[n1].append((value, n2))
            adjList[n2].append((1/value, n1))
        
        visited = set()

        def dfs(i, dest, currSum):
            if i == dest:
                return currSum
            
            visited.add(i)

            for weight, neighbour in adjList[i]:
                if neighbour not in visited:
                    pathSum = dfs(neighbour, dest, currSum * weight)
                    if pathSum > -1.0:
                        visited.remove(i)
                        return pathSum
            
            visited.remove(i)

            return -1.0
        
        res = []
        for src, dest in queries:
            if src not in adjList or dest not in adjList:
                res.append(-1.0)
            else:
                res.append(dfs(src, dest, 1.0))
            
        return res
        



        




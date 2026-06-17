class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # convert edges array into adjacency list O(E)
        adjList = {}
        for edge in edges:
            a, b = edge[0], edge[1]
            if a not in adjList:
                adjList[a] = [b]
            else:
                adjList[a].append(b)
            if b not in adjList:
                adjList[b] = [a]
            else:
                adjList[b].append(a)
        # for every node, run dfs through the node
        # if node visited, do not visit it again
        visited = set()
        res = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if node not in adjList:
                return
            neighbours = adjList[node]
            for neighbour in neighbours:
                dfs(neighbour)
        
        for node in range(n):
            if node not in visited:
                res += 1
            dfs(node)
        return res
        

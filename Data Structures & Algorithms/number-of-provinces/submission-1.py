class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # we want the number of connected components
        # union (i, j) together
        # find the number of distinct roots
        n = len(isConnected)
        rank = [1] * n
        parent = [i for i in range(n)]

        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        
        def union(i, j):
            pi, pj = find(i), find(j)
            ri, rj = rank[pi], rank[pj]

            if pi != pj:
                if ri >= rj:
                    rank[pi] += rj
                    parent[pj] = pi
                else:
                    rank[pj] += ri
                    parent[pi] = pj

        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)
        
        res = 0

        for i in range(n):
            if find(i) == i:
                res += 1
        
        return res
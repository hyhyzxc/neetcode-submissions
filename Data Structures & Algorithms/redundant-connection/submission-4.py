class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        
        def union(i ,j):
            r1, r2 = find(i), find(j)
            if rank[r1] > rank[r2]:
                rank[r1] += rank[r2]
                parent[r2] = r1
            else:
                rank[r2] += rank[r1]
                parent[r1] = r2
        
        def isConnected(i, j):
            return find(i) == find(j)
        
        for n1, n2 in edges:
            if isConnected(n1, n2):
                return [n1, n2]
            else:
                union(n1, n2)
                

            

            

            

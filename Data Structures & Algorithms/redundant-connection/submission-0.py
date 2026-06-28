class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)

            if rx == ry:
                return [x, y]
            
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            
            size[rx] += size[ry]
            parent[ry] = rx
            return []
        
        for edge in edges:
            res = union(edge[0], edge[1])
            if res:
                return res 
            

from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for i in range(n)]
        parent = [i for i in range(n)]

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return
            
            r1, r2 = rank[i], rank[j]
            if r1 >= r2:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
        
        for i, j in edges:
            union(i, j)
        
        res = 0
        for i in range(n):
            if find(i) == i:
                res += 1
        
        return res


        
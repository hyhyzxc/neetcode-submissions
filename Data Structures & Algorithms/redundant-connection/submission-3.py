class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        ranks = [1 for i in range(n + 1)]

        def union(i, j):
            r1, r2 = ranks[i], ranks[j]
            
            if r1 >= r2:
                r1 += r2
                ranks[i] = r1
                parents[j] = i
            else:
                r2 += r1
                ranks[j] = r2
                parents[i] = j
        
        def find(i):
            while i != parents[i]:
                parents[i] = parents[parents[i]]
                i = parents[i]
            
            return i
        
        for edge in edges:
            i, j = edge[0], edge[1]
            r1, r2 = find(i), find(j)
            if r1 == r2:
                return [i, j]
            union(r1, r2)
            

            

            

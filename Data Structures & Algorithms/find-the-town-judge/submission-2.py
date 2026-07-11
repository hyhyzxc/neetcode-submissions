from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
    # 2 <-3 -> 1
    #     |
    #     4
        inDegrees = defaultdict(int)
        outDegrees = defaultdict(int)
        hasOutgoingEdge = set()

        for dest, src in trust:
            inDegrees[dest] += 1
            outDegrees[src] += 1
        
        for node in range(1, n+1):
            if inDegrees[node] == 0 and outDegrees[node] == n - 1:
                return node
        
        return -1

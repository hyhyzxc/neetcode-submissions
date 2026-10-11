"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        visited = set()

        if not node:
            return None

        def dfs(curr):
            if not curr:
                return None

            if curr not in nodeMap:
                nodeMap[curr] = Node(curr.val, [])
            
            clone = nodeMap[curr]
            visited.add(curr)

            for neighbour in curr.neighbors:
                if neighbour not in visited:
                    dfs(neighbour)
                    visited.add(neighbour)
                clone.neighbors.append(nodeMap[neighbour])
        
        dfs(node)
        return nodeMap[node]

        
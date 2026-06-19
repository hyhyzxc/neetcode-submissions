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
        if not node:
            return None
            
        if not node.neighbors:
            return Node(node.val, [])

        clonedMap = {}
        stack = [node]

        while stack:
            curr = stack.pop()
            if curr not in clonedMap:
                currCloned = Node(curr.val, [])
            else:
                currCloned = clonedMap[curr]
            
            for neighbor in curr.neighbors:
                if neighbor not in clonedMap:
                    neighborCloned = Node(neighbor.val, [])
                    clonedMap[neighbor] = neighborCloned
                    currCloned.neighbors.append(neighborCloned)
                    stack.append(neighbor)
                else:
                    currCloned.neighbors.append(clonedMap[neighbor])

                
        
        return clonedMap[node]

        


        
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # bfs to add all nodes in a level
        if not root:
            return None
            
        queue = deque([root])

        while queue:
            currLevel = []
            while queue:
                currLevel.append(queue.popleft())
            
            levelSize = len(currLevel)

            for i in range(levelSize):
                if i < levelSize - 1:
                    currLevel[i].next = currLevel[i+1]
            
            for node in currLevel:
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
        
        return root
        
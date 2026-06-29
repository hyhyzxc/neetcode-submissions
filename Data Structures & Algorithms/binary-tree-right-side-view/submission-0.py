# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([(root)])

        while queue:
            nodesInLevels = []
            while queue:
                nodesInLevels.append(queue.popleft())
            
            if nodesInLevels:
                res.append(nodesInLevels[-1].val)
            
            for node in nodesInLevels:
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
        
        return res
    
        
        
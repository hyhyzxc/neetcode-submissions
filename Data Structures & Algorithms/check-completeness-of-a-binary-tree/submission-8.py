# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if curr == None:
                while queue:
                    next = queue.popleft()
                    if next != None:
                        return False
                
                return True
            
            queue.append(curr.left)
            queue.append(curr.right)

        
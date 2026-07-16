# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, root.val)])
        res = 0
        while queue:
            node, currSum = queue.popleft()
            if not node.left and not node.right:
                res += currSum
            
            if node.left:
                queue.append((node.left, currSum * 10 + node.left.val))
            
            if node.right:
                queue.append((node.right, currSum * 10 + node.right.val))
        
        return res



            

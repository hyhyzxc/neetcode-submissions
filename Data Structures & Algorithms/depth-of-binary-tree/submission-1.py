# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        if not root:
            return 0
        stack = [(root, 1)]

        while stack:
            curr, depth = stack.pop()
            stack.append((curr.left, depth + 1)) if curr.left else None
            stack.append((curr.right, depth + 1)) if curr.right else None

            if depth > maxDepth:
                maxDepth = depth
        
        return maxDepth

        
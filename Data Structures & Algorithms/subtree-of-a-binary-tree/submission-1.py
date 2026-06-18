# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checkIfSubRoot(root, subRoot):
            if (root and not subRoot) or (not root and subRoot):
                return False
            
            if not root and not subRoot:
                return True
            
            if root.val != subRoot.val:
                return False
            
            return checkIfSubRoot(root.left, subRoot.left) and checkIfSubRoot(root.right, subRoot.right)
        
        stack = [root]
        while stack:
            curr = stack.pop()
            stack.append(curr.left) if curr.left else None
            stack.append(curr.right) if curr.right else None
            if curr.val == subRoot.val:
                if checkIfSubRoot(curr, subRoot):
                    return True
        
        return False
        
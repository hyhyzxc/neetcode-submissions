# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def isLeaf(root):
            return not root.left and not root.right
        
        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.left)
            dfs(curr.right)

            if curr.left and isLeaf(curr.left) and curr.left.val == target:
                curr.left = None
            
            if curr.right and isLeaf(curr.right) and curr.right.val == target:
                curr.right = None
        
        dfs(root)
        if root and isLeaf(root) and root.val == target:
            return None
        return root
            

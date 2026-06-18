# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def flipChildren(curr):
            if not curr:
                return None
            if not curr.left and not curr.right:
                return curr

            flipChildren(curr.left)
            flipChildren(curr.right)

            temp = curr.right
            curr.right = curr.left
            curr.left = temp

            return curr
        
        return flipChildren(root)
        

        
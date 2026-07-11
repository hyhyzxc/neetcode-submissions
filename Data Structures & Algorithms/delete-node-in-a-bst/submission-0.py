# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
                    #         8
                    #       3.  9
                    #     2.  6
                    #    1   5. 7
                    #       4
                    #         8
                    #       6.  9
                    #     2.  7
                    #    1   5
                    #       4
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root
                           
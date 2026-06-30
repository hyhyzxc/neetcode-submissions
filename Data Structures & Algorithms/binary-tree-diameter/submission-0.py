# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def findDiameter(root):
            nonlocal res
            if not root:
                return -1
            
            left = findDiameter(root.left)
            right = findDiameter(root.right)
            res = max(res, left + right + 2)
            res = max(res, max(left, right) + 1)

            return max(left, right) + 1

        findDiameter(root)
        return res

        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        currCount = 0
        res = 0

        def inOrder(root):
            nonlocal currCount
            nonlocal res

            if not root:
                return
            
            inOrder(root.left)
            currCount += 1
            if currCount == k:
                res = root.val
                return
            inOrder(root.right)
        
        inOrder(root)
        return res
        
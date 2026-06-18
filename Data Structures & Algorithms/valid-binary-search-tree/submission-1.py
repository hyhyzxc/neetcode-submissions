# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        if not root or (not root.left and not root.right):
            return True

        def preOrder(root):
            if not root:
                return
            preOrder(root.left)
            nodes.append(root.val)
            preOrder(root.right)
        
        preOrder(root)

        prev = nodes[0]
        length = len(nodes)
        for i in range(1, length):
            if nodes[i] <= prev:
                return False
            prev = nodes[i]
        
        return True
        
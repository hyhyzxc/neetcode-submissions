# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        if not root.left and not root.right:
            return root.val
        
        #case 1: include current node value, add left if left > 0 and add right if right > 0
        #case 2: don't include current node, only add left
        #case 3: don't include current node, only add right
        #case 4: include only current node

        def dfs(currNode, currSum):
            nonlocal res

            if not currNode:
                return res

            res = max(currNode.val, res) #case 4

            extra = 0
            
            left = dfs(currNode.left, 0) if currNode.left else min(0, currNode.val)
            right = dfs(currNode.right, 0) if currNode.right else min(0, currNode.val)

            res = max(left, res)
            res = max(right, res)

            if left > 0:
                res = max(left + currNode.val, res)
            
            if right > 0:
                res = max(right + currNode.val, res)
            
            if left > 0 and right > 0:
                res = max(left + right + currNode.val, res)
            
            possibles = [left + currNode.val, right + currNode.val, currNode.val]
            return max(possibles)
        
        dfs(root, 0)
        return res



            
            
            
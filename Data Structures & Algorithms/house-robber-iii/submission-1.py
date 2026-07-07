# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}

        def dfs(root, canRob):
            if not root:
                return 0
            
            if (root, canRob) in dp:
                return dp[(root, canRob)]
            
            res = 0
            if canRob:
                robCurr = dfs(root.left, not canRob) + dfs(root.right, not canRob) + root.val
                skipCurr = dfs(root.left, canRob) + dfs(root.right, canRob)
                res = max(robCurr, skipCurr) 
            else:
                res = max(res, dfs(root.left, not canRob) + dfs(root.right, not canRob))
            
            dp[(root, canRob)] = res
            return res

        dfs(root, True)
        return dp[(root, True)]

        
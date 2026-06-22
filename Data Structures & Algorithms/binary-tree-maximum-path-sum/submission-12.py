class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res, left + right + node.val)

            path = node.val + max(left, max(right, 0))
            res = max(res, path)

            return path
        
        dfs(root)
        return res


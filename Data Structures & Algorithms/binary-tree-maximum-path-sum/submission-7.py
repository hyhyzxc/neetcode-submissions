class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Best path where this node is the highest turning point
            res = max(res, node.val + left + right)

            # Return best one-sided path to parent
            return node.val + max(left, right)

        dfs(root)
        return res
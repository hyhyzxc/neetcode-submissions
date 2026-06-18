# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        levelMap = defaultdict(list)

        queue = deque([(root, 0)])

        while queue:
            curr, level = queue.popleft()
            levelMap[level].append(curr.val)

            queue.append((curr.left, level + 1)) if curr.left else None
            queue.append((curr.right, level + 1)) if curr.right else None
        
        maxLevel = max(levelMap.keys())

        for i in range(maxLevel + 1):
            res.append(levelMap[i])
        return res





        
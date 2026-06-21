# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(curr):
            if not curr:
                res.append("N")
                return
                
            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        
        dfs(root)
        print(res)
        return ','.join(res)
  
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #1,2,N,N,3,4,N,N,5,N,N
        nodes = data.split(',')
        if not nodes or nodes[0] == "N":
            return None
        
        currIndex = 0
        
        def dfs():
            nonlocal currIndex

            if currIndex >= len(nodes):
                return None

            curr = nodes[currIndex]
            if curr == "N":
                currIndex += 1
                return None
            
            currNode = TreeNode(int(curr), None, None)
            currIndex += 1

            currNode.left = dfs()
            currNode.right = dfs()
            return currNode
            


            





        
        dfs()
        return root


        


        



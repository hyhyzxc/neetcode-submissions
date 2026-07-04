"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        originalToCopyMap = {}
        originalCurr = head
        copyCurr = Node(head.val, None, None)
        copyHead = copyCurr
        originalToCopyMap[originalCurr] = copyCurr

        while originalCurr:
            nextOriginal = originalCurr.next
            if nextOriginal:
                copyCurr.next = Node(nextOriginal.val, None, None)
                originalToCopyMap[nextOriginal] = copyCurr.next
            originalCurr = nextOriginal
            copyCurr = copyCurr.next
        
        for originalNode in originalToCopyMap:
            randomNode = originalNode.random
            if randomNode:
                copyNode = originalToCopyMap[originalNode]
                copyNode.random = originalToCopyMap[randomNode]
        
        return copyHead
        




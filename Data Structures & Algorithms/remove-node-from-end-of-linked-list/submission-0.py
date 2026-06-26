# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listSize = 0
        curr = head
        while curr:
            listSize += 1
            curr = curr.next
        
        target = listSize - n
        if listSize <= 1:
            return None
        
        if target == 0:
            return head.next
        
        curr = head
        for i in range(target - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head

        
        

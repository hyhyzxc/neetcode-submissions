# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummyHead -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 
        # 3 -> 2 -> 1 -> dummyHead | 4 -> 5 -> 6 
        # 3 -> 2 -> 1 -> dummyHead | 6 -> 5 -> 4
        # 1.next = 6
        if not head.next:
            return head
        
        # this function return the new head of a linked list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # returns (newHead, nextHead)
        def reverseKNodes(head):
            if not head:
                return (None, None, None)

            prev = None
            curr = head
            counter = 0

            while curr and counter != k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                counter += 1

            return (prev, next)
        
        # reverseKNodes(1) -> (3, 4)
        newHead = None
        prevHead = None
        curr = head

        for j in range(math.floor(n/k)):
            currHead, nextHead = reverseKNodes(curr)
            if j == 0:
                newHead = currHead
            if prevHead:
                prevHead.next = currHead
            
            prevHead = currHead
            for i in range(k - 1):
                prevHead = prevHead.next
            
            curr = nextHead
        
        prevHead.next = nextHead
        return newHead
        

            


        




        

        

        

        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6, left = 2, right = 5
                        
        if left == right:
            return head

        dummyHead = ListNode(0, head)

        curr, prev = dummyHead, None
        count = 0 

        while count < left:
            prev = curr
            curr = curr.next
            count += 1
        
        beforeLeftNode = prev
        leftNode = curr
        
        while count <= right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        
        beforeLeftNode.next = prev
        leftNode.next = curr

        return dummyHead.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # reverse linked list 2 with head2 as first node
        curr = head2
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev
        # keep picking 1 element from head1 then head2
        
        head1 = head
        while head1 and head2:
            head1Next = head1.next
            head1.next = head2
            head1 = head1Next

            head2Next = head2.next
            head2.next = head1
            head2 = head2Next
        
        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        ptr1, ptr2 = l1, l2

        ptr3 = ListNode(-1, None)
        resHead = ptr3

        while ptr1 and ptr2:
            currSum = ptr1.val + ptr2.val + carry
            if currSum >= 10:
                carry = 1
                currSum -= 10
            else:
                carry = 0
            
            ptr3.next = ListNode(currSum, None)
            
            ptr1, ptr2, ptr3 = ptr1.next, ptr2.next, ptr3.next
        
        while ptr1:
            currSum = ptr1.val + carry
            if currSum >= 10:
                carry = 1
                currSum -= 10
            else:
                carry = 0
            ptr3.next = ListNode(currSum, None)

            ptr1, ptr3 = ptr1.next, ptr3.next
        
        while ptr2:
            currSum = ptr2.val + carry
            if currSum >= 10:
                carry = 1
                currSum -= 10
            else:
                carry = 0
            ptr3.next = ListNode(currSum, None)

            ptr2, ptr3 = ptr2.next, ptr3.next
        
        if carry:
            ptr3.next = ListNode(1, None)
        
        return resHead.next
        



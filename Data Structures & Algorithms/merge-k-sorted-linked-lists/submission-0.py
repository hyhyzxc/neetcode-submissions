# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        heap = [] #stores (node value, list index)

        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        if not heap:
            return None
        
        val, index = heapq.heappop(heap)
        root = lists[index]
        lists[index] = lists[index].next
        if lists[index]:
            heapq.heappush(heap, (lists[index].val, index))
        curr = root

        while heap:
            val, index = heapq.heappop(heap)
            curr.next = lists[index]
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
            curr = curr.next
        
        return root
        


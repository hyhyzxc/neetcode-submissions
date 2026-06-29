import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        l = 0 
        r = k - 1

        while r < len(nums):
            toRemove = nums[l]
            res.append(-heap[0][0])

            if toRemove == -heap[0][0]:
                heapVal, heapIndex = -heap[0][0], heap[0][1]
                while heap and heapIndex <= l:
                    heapq.heappop(heap)
                    if heap:
                        heapVal, heapIndex = -heap[0][0], heap[0][1]
            
            l += 1
            r += 1

            if r < len(nums):
                heapq.heappush(heap, (-nums[r], r))
        
        return res
        


                    



        
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        l = 0
        res = []

        for r in range(len(nums)):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if r - l + 1 >= k:
                res.append(nums[queue[0]])
                l += 1
            
            if queue[0] < l:
                queue.popleft()
            
            r += 1
        
        return res
            






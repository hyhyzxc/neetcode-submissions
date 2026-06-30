class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, height in enumerate(heights):
            j = i
            while stack and height < stack[-1][1]:
                prevIndex, prevHeight = stack.pop()
                res = max(res, (i - prevIndex) * prevHeight)
                j = prevIndex
            
            stack.append((j, height))
        
        for prevIndex, prevHeight in stack:
            res = max(res, (len(heights) - prevIndex) * prevHeight)
        
        return res
        

        






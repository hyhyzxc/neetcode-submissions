class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            length = r - l
            
            leftHeight = heights[l]
            rightHeight = heights[r]

            height = min(leftHeight, rightHeight)
            
            res = max(res, height * length)

            if leftHeight <= rightHeight:
                l += 1
            
            else:
                r -= 1
            
        return res
        
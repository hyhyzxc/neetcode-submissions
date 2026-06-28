class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0 for i in range(n)]
        maxRight = [0 for i in range(n)]

        currMax = height[0]
        for i in range(1, n):
            currMax = max(currMax, height[i-1])
            maxLeft[i] = currMax
        
        currMax = height[-1]
        for i in range(n-2, -1, -1):
            currMax = max(currMax, height[i+1])
            maxRight[i] = currMax
        
        res = 0

        for i in range(n):
            res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        
        return res
        
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k-1

        bestIndex, res = 0, float("inf")
        if k == 1:
            for i, num in enumerate(arr):
                if abs(num - x) < res:
                    res = abs(num - x)
                    bestIndex = i
            return [arr[bestIndex]]
            

        prev = abs(arr[l] - x)
        while r + 1 < len(arr) and abs(arr[r+1] - x) < prev:
            r += 1
            l += 1
            prev = abs(arr[l] - x)
        
        return arr[l:r+1]
        
        

        
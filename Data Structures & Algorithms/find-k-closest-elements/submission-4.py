class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # answer would always be a subarray

        l, r = 0, k - 1

        while r < len(arr) - 1:
            diff = abs(arr[r + 1] - x) - abs(arr[l] - x)
            if diff > 0:
                return arr[l : r+1]
            elif diff < 0:
                l += 1
                r += 1
            else:
                if arr[r + 1] == arr[l]:
                    l += 1
                    r += 1
                else:
                    return arr[l: r + 1]
                
        
        return arr[l: r + 1]

        
        

        
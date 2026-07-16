class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        n = len(arr)
        total = sum(arr[:k])
        res = 0

        while r < n:
            if total / k >= threshold:
                res += 1
            
            r += 1

            if r >= n:
                return res
            
            total += arr[r]
            total -= arr[l]
            l += 1
        
        return res

            

        
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x//2 + 1

        # l = 0, r = 6, m = 3
        # l = 4, r = 6, m = 5
        # l = 4, r = 4, m = 4
        # l = 4, r = 3, m = 3

        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1
        
        return r
        
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hoursTaken = self.hoursToFinishEating(piles, mid)

            if hoursTaken > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
        
    
    def hoursToFinishEating(self, piles, numToEat):
        res = 0

        for pile in piles:
            res += math.ceil(pile / numToEat)
        
        return res


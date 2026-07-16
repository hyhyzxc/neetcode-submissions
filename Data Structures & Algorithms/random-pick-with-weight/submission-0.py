import random
class Solution:

    def __init__(self, w: List[int]):
        self.weights = [0] * len(w)
        self.weights[0] = w[0]
        self.total = sum(w)
        
        for i in range(1, len(w)):
            self.weights[i] = self.weights[i-1] + w[i]

        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        curSum = 0

        l, r = 0, len(self.weights) - 1
        while l <= r:
            m = (l + r) // 2
            if self.weights[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
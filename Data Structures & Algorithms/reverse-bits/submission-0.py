class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        shift = 31
        while n != 0:
            curr = n % 2
            curr = curr << shift
            res = res | curr
            n = n >> 1
            shift -= 1
        return res

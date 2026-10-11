class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        res = 0

        def isValid(counts):
            return sum(counts) - max(counts) <= k
        
        l, r = 0, 0

        while r < len(s):
            curr = s[r]
            counts[ord(curr) - ord('A')] += 1

            while not isValid(counts):
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
        
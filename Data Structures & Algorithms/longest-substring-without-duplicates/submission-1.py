from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countMap = defaultdict(int)
        res = 0
        l, r = 0, 0
        
        while r < len(s):
            while countMap[s[r]] > 0:
                countMap[s[l]] -= 1
                l += 1
            
            countMap[s[r]] += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res








        

        
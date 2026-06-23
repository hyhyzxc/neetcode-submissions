from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = defaultdict(int)
        res = 0
        strLength = len(s)

        if strLength <= 1:
            return strLength

        l = 0
        r = 1
        charMap[s[l]] += 1

        while r < strLength:
            currChar = s[r]
            charMap[currChar] += 1

            while charMap[currChar] > 1:
                charMap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res






        

        
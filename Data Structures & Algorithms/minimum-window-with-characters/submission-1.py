from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        strLength = len(s)
        currMin = strLength + 1
        res = ""
        targetMap = defaultdict(int)
        for char in t:
            targetMap[char] += 1
        
        charMap = defaultdict(int)
        
        def checkIfMeetTarget(charMap, targetMap):
            for char in targetMap:
                if charMap[char] < targetMap[char]:
                    return False
            
            return True
        
        l = r = 0

        while r < strLength:
            charMap[s[r]] += 1
            
            while l <= r and checkIfMeetTarget(charMap, targetMap):
                if (r - l + 1) < currMin:
                    res = s[l:r+1]
                    currMin = min(currMin, r - l + 1)
                charMap[s[l]] -= 1
                l += 1
            
            r += 1
        
        return res
            


        


        

        
        

        